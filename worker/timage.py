from kafka import KafkaConsumer

# Save the image
import cv2
import json
import redis
import time
import numpy as np


class imageProcesser():
    def __init__(self):
        print('hello')
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

                
            path = '/home/generated/'  
            #path = '/home/microshak/Source/'
            imgName = path + fileName + ".png"
            thumbName =path + fileName + "_thumb.png"
            # Create a blank image
            img = np.zeros((500, 500, 3), dtype=np.uint8)

            # Draw text on the image
            cv2.putText(img, prompt, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)


            cv2.imwrite(thumbName, img)
            
            
            imageInfo["status"] = "ready"
            updated = json.dumps(imageInfo)
            self.imageredis.set(fileName,updated)

print("DDDDDDDDDDDDDDDDDDDDDDDDDD")

ip = imageProcesser()
while True == True:
    print("starting")
    ip.processImage()
    print("sleeping")
    
    time.sleep(5)
