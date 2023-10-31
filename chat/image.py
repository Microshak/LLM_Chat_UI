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




common =  common()
keras.mixed_precision.set_global_policy("float32")



im = Blueprint('im', __name__)


gpus = tf.config.list_physical_devices('GPU')



@im.route('/image', methods=['GET','POST'])
def image():
    tf.device("/cpu:0")

    model = keras_cv.models.StableDiffusion(img_height=512, 
                                        img_width=512,
                                        jit_compile=True)
    model.cdevice = "cpu:0"

    with tf.device('/cpu:0'):
    # Create images from text
        images = model.text_to_image(prompt="A painting of a city by vincent van gogh, highly detailed, sharp focused, impressionism, oil painting", batch_size=1)

        _, im_bytes_np = cv2.imencode('.png', images[0])
        bytes_str = im_bytes_np.tobytes()
        response = flask.make_response(bytes_str)
        response.headers.set('Content-Type', 'image/png')
    
        return response