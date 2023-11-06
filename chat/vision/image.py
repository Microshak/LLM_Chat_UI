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
from kafka import  KafkaProducer


#from flask import Flask
#from flask_apscheduler import APScheduler
common =  common()
keras.mixed_precision.set_global_policy("float32")

im = Blueprint('im', __name__ ,url_prefix='/api')

gpus = tf.config.list_physical_devices('GPU')

redis = common.imageredis

#@im.route('/historicimage', methods=['GET'])
#def historicimage():
    

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092']
)




@im.route('/getImages', methods=['GET'])
def queueimage():
    
    RET = {}
    # get all keys
    keys = redis.keys()
    ret = []
    # iterate over keys and get values
    for key in keys:
        value = redis.get(key)
        print(key, value)
        temp = json.dumps(value)
        temp['thumb'] = f'./{key}_thumb.png'
        temp['image'] = f'./{key}.png'
        ret.append(temp)
    return ret


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

