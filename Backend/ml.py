from __future__ import absolute_import, division, print_function, unicode_literals
from PIL import Image

import tensorflow as tf

import os
import numpy as np
import matplotlib.pyplot as plt

# loaded = tf.saved_model.load("./save/model")


# base_dir = "../Downloads/flower_photos"

# IMAGE_SIZE = 224
# BATCH_SIZE = 64

# datagen = tf.keras.preprocessing.image.ImageDataGenerator(
#     rescale=1./255, 
#     validation_split=0.2)

# train_generator = datagen.flow_from_directory(
#     base_dir,
#     target_size=(IMAGE_SIZE, IMAGE_SIZE),
#     batch_size=BATCH_SIZE, 
#     subset='training')
# image_batch, label_batch = next(train_generator)

# print(loaded.predict(image_batch[0]))

IMAGE_SIZE = 224
IMG_SHAPE = (IMAGE_SIZE, IMAGE_SIZE, 3)

base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                              include_top=False, 
                                              weights='imagenet')

base_model.trainable = False

model = tf.keras.Sequential([
  base_model,
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.GlobalAveragePooling2D(),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.load_weights("./tim_weights.hdf5")
# print(model)

def get_prediction(imgName):
	img = Image.open("./" + imgName).resize((IMAGE_SIZE, IMAGE_SIZE))
	#print(img)
	img.load()
	#print("IMG:", img)
	data = np.asarray(img, dtype="int32") / 255
	data = np.array([data])
	#print("DATA: ", data)
	#print("SHAPE:", data.shape)
	return model.predict(data)