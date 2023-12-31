# Model

import tensorflow as tf
from tensorflow import keras
import  keras_cv
keras.mixed_precision.set_global_policy("float32")

gpus = tf.config.list_physical_devices('GPU')

if gpus:
    for gpu in gpus:
        tf.config.experimental.set_virtual_device_configuration(gpu,[tf.config.experimental.VirtualDeviceConfiguration(memory_limit=2096)])
        print(gpu)

tf.device("/cpu:0")

# Visualization
import matplotlib.pyplot as plt

# Save the image
from PIL import Image


model = keras_cv.models.StableDiffusion(img_height=512, 
                                        img_width=512,
                                        jit_compile=True)


#https://github.com/basujindal/stable-diffusion/blob/main/optimizedSD/optimized_txt2img.py
model.cdevice = "cpu:0"
def plot_images(images):
    # Set figure size
    plt.figure(figsize=(20, 20))
    # Loop through each image
    for i in range(len(images)):
        # Subplot setup
        ax = plt.subplot(1, len(images), i + 1)
        # Plot each image
        plt.imshow(images[i])
        # Do not show axis
        plt.axis("off")

with tf.device('/cpu:0'):
# Create images from text
    images = model.text_to_image(prompt="A painting of a city by vincent van gogh, highly detailed, sharp focused, impressionism, oil painting",
                             batch_size=1)

    Image.fromarray(images[0]).save("van_gogh_city1.png")
