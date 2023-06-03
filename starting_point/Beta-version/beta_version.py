#!/usr/bin/env python
# coding: utf-8
import matplotlib.pyplot as plt
from keras.layers import Conv2D, UpSampling2D, InputLayer, Conv2DTranspose, Input, Conv2D, UpSampling2D, MaxPooling2D
from keras.layers import Activation, Dense, Dropout, Flatten
from keras.layers import BatchNormalization
from keras.models import Sequential
from keras.callbacks import TensorBoard
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import array_to_img, img_to_array, load_img
from skimage.color import rgb2lab, lab2rgb, rgb2gray, xyz2lab
from skimage.io import imsave
import numpy as np
import os
import random
import tensorflow as tf
from skimage import img_as_ubyte
import torch
import keras
import torch
import keras
#from tensorflow.keras.layers import Input, Conv2D, UpSampling2D, MaxPooling2D
import matplotlib.pyplot as plt
import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from skimage.color import rgb2lab, lab2rgb
from skimage.io import imsave
import tensorflow as tf
from skimage import img_as_ubyte
from PIL import Image
from keras import optimizers
from sklearn.model_selection import train_test_split


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
for filename in os.listdir('starting_point/Beta-version/Paisaje_train/'):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        img = Image.open('starting_point/Beta-version/Paisaje_train/' + filename)
        img = img.resize((256, 256))  # Asegurar que todas las imágenes tengan las mismas dimensiones
        if img.mode == 'L':
            img = np.expand_dims(img, axis=2)  # Agregar una dimensión de canal
            img = np.repeat(img, 3, axis=2)
        X.append(img_to_array(img))
print("LLISTA-------------------", len(X))

# Verificar que todas las imágenes tengan la misma forma
shapes = [img.shape for img in X]
unique_shapes = set(shapes)
print(unique_shapes)
if len(unique_shapes) > 1:
    print("Las imágenes no tienen la misma forma después de redimensionar.")

X = np.array(X, dtype=float)

# Split data into training and testing sets
Xtrain, Xtest = train_test_split(X, test_size=0.05, random_state=42)
Xtrain = 1.0 / 255 * Xtrain
Xtest = 1.0 / 255 * Xtest

# Crear una sesión de TensorFlow y asignar la GPU como dispositivo de ejecución
with tf.device('/GPU:0'):
    model = Sequential()
    model.add(InputLayer(input_shape=(256, 256, 1)))
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    # ... rest of the model ...

    optimizerAda = optimizers.Adagrad(lr=0.001)
    model.compile(optimizer=optimizerAda, loss='mse')

    # Image transformer data augmentation
    datagen = ImageDataGenerator(
        shear_range=0.2,
        zoom_range=0.2,
        rotation_range=20,
    )

    batch_size = 20
    def image_a_b_gen(batch_size):
        for batch in datagen.flow(Xtrain, batch_size=batch_size):
            lab_batch = rgb2lab(batch)
            X_batch = lab_batch[:, :, :, 0]
            Y_batch = lab_batch[:, :, :, 1:] / 128
            yield (X_batch.reshape(X_batch.shape + (1,)), Y_batch)

    # Train model
    tensorboard = TensorBoard(log_dir="output/first_run")
    history = model.fit_generator(
    image_a_b_gen(batch_size),
    callbacks=[tensorboard],
    epochs=5,
    steps_per_epoch=10,
    validation_data=(Xtest, None) ) # Use validation data instead of validation_split


    # Save model
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model.h5")

    # Process history
    train_loss = history.history['loss']
    val_loss = history.history['val_loss']

    # Plot learning curves
    plt.figure(figsize=(12, 6))
    plt.plot(range(1, len(train_loss) + 1), train_loss, label='Training Loss')
    plt.plot(range(1, len(val_loss) + 1), val_loss, label='Validation Loss')
    plt.xlabel('Iteration')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('starting_point/Beta-version/result_curves/learning_curves-paisaje.png')
    plt.close()


    # Test images
    Xtest = rgb2lab(1.0 / 255 * X[split:])[:, :, :, 0]
    Xtest = Xtest.reshape(Xtest.shape + (1,))
    Ytest = rgb2lab(1.0 / 255 * X[split:])[:, :, :, 1:]
    Ytest = Ytest / 128
    print(model.evaluate(Xtest, Ytest, batch_size=batch_size))

    color_me = []

    for filename in os.listdir('starting_point/Beta-version/Val_beta/'):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            img = Image.open('starting_point/Beta-version/Val_beta/' + filename)
            img = img.resize((256, 256))
            if img.mode == 'L':
                img = np.expand_dims(img, axis=2)  # Agregar una dimensión de canal
                img = np.repeat(img, 3, axis=2)  
            color_me.append(img_to_array(img))

    # Verificar las formas de los elementos en la lista
    for i, img_array in enumerate(color_me):
        print(f"Forma del elemento {i}: {img_array.shape}")

    #color_me[2] = np.delete(color_me[2], 3, axis=2)
    #print(f"Forma corregida del elemento 2: {color_me[2].shape}")

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
   
    imsave("starting_point/Beta-version/result_rural/img_" + str(i) + ".png", cur)