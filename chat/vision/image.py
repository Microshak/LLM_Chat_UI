from flask import Flask, redirect, url_for, request, Blueprint

from flask import Blueprint
from chat.common import common

import tensorflow as tf
from tensorflow import keras
import  keras_cv
import matplotlib.pyplot as plt

# Save the image
from PIL import Image
import flask
import cv2
import json
import os

import datetime


#from flask import Flask
#from flask_apscheduler import APScheduler
common =  common()
keras.mixed_precision.set_global_policy("float32")

im = Blueprint('im', __name__ ,url_prefix='/api')

gpus = tf.config.list_physical_devices('GPU')

redis = common.imageredis

#@im.route('/historicimage', methods=['GET'])
#def historicimage():
from kafka import KafkaConsumer, KafkaProducer
    

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    security_protocol="SSL"
)

consumer = KafkaConsumer(
    client_id="client3",
        group_id="CONSUMER_GROUP_CALC",
        bootstrap_servers="localhost:9092",
        security_protocol="SSL",
        max_poll_records=1,
        auto_offset_reset='earliest',
        session_timeout_ms=6000,
        heartbeat_interval_ms=3000,
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)




@im.route('/queueimage', methods=['POST'])
def queueimage():
    tf.device("/cpu:0")
    
    data = request.json
    img_height = data["img_height"]
    img_width = data["img_width"]
    prompt = data["prompt"]
    
    d = datetime.datetime.now()
    t0 = datetime.datetime(2023, 10, 10)
    ticks = str(int((d - t0).total_seconds()))

    fileName=ticks
    value = json.dumps({"prompt":prompt,"img_height":img_height, "img_width":img_width, "status":"queued"})
    imageInfo = value
    
    redis.set(fileName,imageInfo)
    redis.expire(fileName,86400*7)
    producer.send(
            "image_queue",
            key=fileName,
            value=value
        )

    producer.flush()

def processImage():
    tf.device("/cpu:0")
    consumer.subscribe("image_queue")
    for message in consumer:
        message = f"""
        Message received: {message.value}
        Message key: {message.key}
        Message partition: {message.partition}
        Message offset: {message.offset}
        """
        fileName = message.key
        img_height = message.value["img_height"]
        img_width = message.value["img_width"]
        prompt = message.value["prompt"]
        imageInfo = message.value
        imageInfo["status"] = "processing"
        redis.set(fileName,imageInfo)

        model = keras_cv.models.StableDiffusion(img_height=img_height, 
                                            img_width=img_width,
                                            jit_compile=True)
        model.cdevice = "cpu:0"

        with tf.device('/cpu:0'):
        # Create images from text
            images = model.text_to_image(prompt=prompt, batch_size=1)
            img = images[0]
            
            thumbheight = 150 # percent of original size
            thumbwidth = int(img.shape[1] * thumbheight / img_height)
            
            dim = (thumbwidth, thumbheight)
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            
            base = im.root_path.replace("/vision","")
            path = os.path.join(base, 'static/img/generated/')  
            imgName = path + fileName + ".png"
            thumbName =path + fileName + "_thumb.png"
            cv2.imwrite(thumbName, resized)
            
            Image.fromarray(images[0]).save(imgName)
            _, im_bytes_np = cv2.imencode('.png', images[0])
            bytes_str = im_bytes_np.tobytes()
            response = flask.make_response(bytes_str)
            response.headers.set('Content-Type', 'image/png')
            
            imageInfo["status"] = "ready"
            redis.set(fileName,imageInfo)