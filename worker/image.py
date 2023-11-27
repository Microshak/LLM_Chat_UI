from kafka import KafkaConsumer, KafkaProducer
import tensorflow as tf
from tensorflow import keras
import  keras_cv
import matplotlib.pyplot as plt

# Save the image
from PIL import Image
import cv2
import json
import redis
import time


class imageProcesser():
    def __init__(self):
        redisURL = os.getenv("redisURL")
        self.imageredis = redis.Redis(host=redisURL, db=2, port=6379, decode_responses=True)

        self.consumer = KafkaConsumer(
            client_id="client3",
                group_id="CONSUMER_GROUP_CALC22",
                bootstrap_servers="localhost:9092",
                max_poll_records=1,
                auto_offset_reset='earliest',
                session_timeout_ms=6000,
                heartbeat_interval_ms=3000,
                value_deserializer=lambda x: json.loads(x.decode("utf-8"))
        )

    def processImage(self):
        tf.device("/cpu:0")
        print('checking kafka')
        self.consumer.subscribe("image_queue")
        for message in self.consumer:
            lamessage = f"""
            Message received: {message.value}
            Message key: {message.key}
            Message partition: {message.partition}
            Message offset: {message.offset}
            """
            print(lamessage)
            
            fileName = message.key.decode()
            mObj = json.loads(message.value)
            img_height = int(mObj["img_height"])
            img_width = int(mObj["img_width"])
            prompt = mObj["prompt"]
            imageInfo = mObj
            imageInfo["status"] = "processing"
            updated = json.dumps(imageInfo)
            self.imageredis.set(fileName,updated)

            model = keras_cv.models.StableDiffusion(img_height=img_height, img_width=img_width, jit_compile=True)
            model.cdevice = "cpu:0"

            with tf.device('/cpu:0'):
            # Create images from text
                images = model.text_to_image(prompt=prompt, batch_size=1)
                img = images[0]
                
                thumbheight = 150 # percent of original size
                thumbwidth = int(img.shape[1] * thumbheight / img_height)
                
                dim = (thumbwidth, thumbheight)
                resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                
                
                path = '/home/generated/'  
                imgName = path + fileName + ".png"
                thumbName =path + fileName + "_thumb.png"
                cv2.imwrite(thumbName, resized)
                
                Image.fromarray(images[0]).save(imgName)
                
                imageInfo["status"] = "ready"
                updated = json.dumps(imageInfo)
                self.imageredis.set(fileName,updated)



ip = imageProcesser()
while True == True:
    print("starting")
    ip.processImage()
    print("sleeping")
    
    time.sleep(5)
