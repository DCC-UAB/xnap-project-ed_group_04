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
from tensorflow.keras.layers import BatchNormalization, Conv2D, InputLayer, UpSampling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import tensorflow as tf
from skimage import img_as_ubyte
from PIL import Image


# Get images
X = []
for filename in os.listdir('starting_point/Beta-version/Paisajes_train/'):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open('starting_point/Beta-version/Paisajes_train/' + filename)
        img = img.resize((256, 256))  # Asegurar que todas las imágenes tengan las mismas dimensiones
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
model.add(Conv2D(512, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(2, (3, 3), activation='tanh', padding='same'))
model.add(UpSampling2D((2, 2)))
model.compile(optimizer='adagrad', loss='mse', metrics=['accuracy'])


#------------------------------------------DATA LOADER--------------------------------------------------------------
# Image transformer   data augmentation
datagen = ImageDataGenerator(
        
       
        shear_range=0.2,
        zoom_range=0.2,
        rotation_range=20,
        horizontal_flip=True, 
        vertical_flip=True)

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
history = model.fit_generator(image_a_b_gen(batch_size), callbacks=[tensorboard], epochs=50, steps_per_epoch=10)

# Save model
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")

# Process history
losses = history.history['loss']
accuracies = history.history['accuracy']

# Plot learning curves
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(range(1, len(losses) + 1), losses)
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(range(1, len(accuracies) + 1), accuracies)
plt.xlabel('Iteration')
plt.ylabel('Accuracy')
plt.title('Training Accuracy')
plt.grid(True)

plt.tight_layout()
plt.savefig('starting_point/Beta-version/result/learning_curves.png')
plt.close()

# Test images
Xtest = rgb2lab(1.0 / 255 * X[split:])[:, :, :, 0]
Xtest = Xtest.reshape(Xtest.shape + (1,))
Ytest = rgb2lab(1.0 / 255 * X[split:])[:, :, :, 1:]
Ytest = Ytest / 128
print(model.evaluate(Xtest, Ytest, batch_size=batch_size))

color_me = []
for filename in os.listdir('starting_point/Beta-version/Paisajes2/'):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open('starting_point/Beta-version/Paisajes2/' + filename)
        img = img.resize((256, 256))
        color_me.append(img_to_array(img))
color_me = np.array(color_me, dtype=float)
color_me = rgb2lab(1.0 / 255 * color_me)[:, :, :, 0]
color_me = color_me.reshape(color_me.shape + (1,))

# Test model
output = model.predict(color_me)
output = output * 128

# Output colorizations
for i in range(len(output)):
    cur = np.zeros((256, 256, 3))
    cur[:, :, 0] = color_me[i][:, :, 0]
    cur[:, :, 1:] = output[i]
    cur = lab2rgb(cur)
   
    imsave("starting_point/Beta-version/result/img_" + str(i) + ".png", cur)
