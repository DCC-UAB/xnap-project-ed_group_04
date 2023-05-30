#!/usr/bin/env python
# coding: utf-8
import matplotlib.pyplot as plt
from keras.layers import Conv2D, UpSampling2D, InputLayer, Conv2DTranspose, Input, Conv2D, UpSampling2D, MaxPooling2D
from keras.layers import Activation, Dense, Dropout, Flatten
from tensorflow.keras.layers import BatchNormalization
from keras.models import Sequential
from keras.callbacks import TensorBoard
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import array_to_img, img_to_array, load_img
from skimage.color import rgb2lab, lab2rgb, rgb2gray, xyz2lab
from skimage.io import imsave
import numpy as np
import os
import random

import tensorflow as tf
from skimage import img_as_ubyte
#from tensorflow.keras.layers import Input, Conv2D, UpSampling2D, MaxPooling2D
import matplotlib.pyplot as plt
import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from skimage.color import rgb2lab, lab2rgb
from skimage.io import imsave
from keras.layers import BatchNormalization, Conv2D, InputLayer, UpSampling2D
from keras.models import Sequential
from keras.callbacks import TensorBoard
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import tensorflow as tf
from skimage import img_as_ubyte
from PIL import Image

# Verificar la disponibilidad de la GPU
if tf.config.experimental.list_physical_devices('GPU'):
    print('Se encontró una GPU')
else:
    print('No se encontró una GPU')

# Configurar TensorFlow para utilizar la GPU disponible
physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
    print('---Configuración de GPU completada--')

# Get images
X = []
for filename in os.listdir('starting_point/Beta-version/Paisatges/'):
    if filename.endswith(".jpg") or filename.endswith(".png") or  filename.endswith(".jpeg"):
        img = Image.open('starting_point/Beta-version/Paisatges/' + filename)
        #print("IMATGE:--------------------", img)
        img = img.resize((256, 256))  # Asegurar que todas las imÃ¡genes tengan las mismas dimensiones
        X.append(img_to_array(img))


X = np.array(X, dtype=float)



# Set up train and test data
split = int(0.95 * len(X))
Xtrain = X[:split]
Xtrain = 1.0 / 255 * Xtrain


model = Sequential()
model.add(InputLayer(input_shape=(256, 256, 1)))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same', strides=2))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same', strides=2))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same', strides=2))
model.add(Conv2D(512, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(512, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(2, (3, 3), activation='tanh', padding='same'))
model.add(UpSampling2D((2, 2)))
model.compile(optimizer='adagrad', loss='mse')


#------------------------------------------DATA LOADER--------------------------------------------------------------
# Image transformer   data augmentation
datagen = ImageDataGenerator(
        
       
        shear_range=0.2,
        zoom_range=0.2,
        rotation_range=20,
        horizontal_flip=False, 
        vertical_flip=False)

# Generate training data
batch_size = 10
def image_a_b_gen(batch_size):
    for batch in datagen.flow(Xtrain, batch_size=batch_size):  #entrena per bloc
        lab_batch = rgb2lab(batch)
        X_batch = lab_batch[:, :, :, 0]
        Y_batch = lab_batch[:, :, :, 1:] / 128
        yield (X_batch.reshape(X_batch.shape + (1,)), Y_batch)  #retorna cada bloc de dades de train


#-------------------------------------------------------------------------------------------------------------------------
# Train model      
tensorboard = TensorBoard(log_dir="output/first_run")
history = model.fit_generator(image_a_b_gen(batch_size), callbacks=[tensorboard], epochs=50, steps_per_epoch=40)

# Save model
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")

# Process history
losses = history.history['loss']


# Plot learning curves
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(range(1, len(losses) + 1), losses)
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.grid(True) 



plt.tight_layout()
plt.savefig('starting_point/Beta-version/learning_curves_gif.png')
plt.close()

gif_path = "starting_point/Beta-version/video-paisatge.gif"
gif_image = Image.open(gif_path)

#gif_image.show()

frames = []
try:
    while True:
        frames.append(gif_image.copy())
        gif_image.seek(len(frames))  # Obtén el siguiente fotograma
except EOFError:
    pass

print("------------------NUM FRAME--------------------------------------------: ", len(frames))


color_me = []
for frame in frames:
    frame = frame.resize((256, 256))
    if len(color_me)==0:
        frame = np.expand_dims(frame, axis=2)  # Agregar una dimensión de canal
        frame = np.repeat(frame, 3, axis=2)  
    color_me.append(img_to_array(frame))

color_me = np.array(color_me, dtype=float)
color_me = rgb2lab(1.0 / 255 * color_me)[:, :, :, 0]
color_me = color_me.reshape(color_me.shape + (1,))
output = model.predict(color_me)
output = output * 128

# Output colorizations
for i in range(len(output)):
    cur = np.zeros((256, 256, 3))
    cur[:, :, 0] = color_me[i][:, :, 0]
    cur[:, :, 1:] = output[i]
    cur = lab2rgb(cur)
   
    imsave("starting_point/Beta-version/result_gif/img_" + str(i) + ".png", cur)

import imageio

output_images = []

for i in range(len(output)):
    cur = np.zeros((256, 256, 3))
    cur[:, :, 0] = color_me[i][:, :, 0]
    cur[:, :, 1:] = output[i]
    cur = lab2rgb(cur)
    cur = img_as_ubyte(cur)  # Convertir a formato de 8 bits (0-255)
    output_images.append(cur)

output_gif_path = 'output/result.gif'
imageio.mimsave(output_gif_path, output_images, duration=0.9)  # Guardar como archivo GIF

print("Archivo GIF guardado en:", output_gif_path)