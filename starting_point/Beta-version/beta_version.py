import matplotlib.pyplot as plt
from keras.layers import Conv2D, UpSampling2D, InputLayer, Conv2DTranspose
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
from PIL import Image, UnidentifiedImageError

# Get images
X = []
desired_shape = (256, 256)  # Tamaño deseado para las imágenes

for filename in os.listdir('starting_point/Beta-version/Paisatges/'):
    try:
        img = load_img('starting_point/Beta-version/Paisatges/' + filename)
        img = img.resize(desired_shape)  # Redimensionar imagen al tamaño deseado
        X.append(img_to_array(img))
    except UnidentifiedImageError:
        print(f"Error al cargar la imagen {filename}")

X = np.stack(X, axis=0)  # Utiliza np.stack() en lugar de np.array()
X = X.astype(float)  # Opcionalmente, puedes convertir el tipo de dato a float

# Set up train and test data
split = int(0.95*len(X))
Xtrain = X[:split]
Xtrain = 1.0/255*Xtrain

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
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(2, (3, 3), activation='sigmoid', padding='same'))
model.add(UpSampling2D((2, 2)))
model.compile(optimizer='adagrad', loss='mse')

# Image transformer  data augmentation
datagen = ImageDataGenerator(
        shear_range=0.2,
        zoom_range=0.2,
        rotation_range=20,
        horizontal_flip=True)

# Generate training data
batch_size = 10

def image_a_b_gen(batch_size):
    for batch in datagen.flow(Xtrain, batch_size=batch_size):
        lab_batch = rgb2lab(batch)
        X_batch = lab_batch[:,:,:,0]
        Y_batch = lab_batch[:,:,:,1:] / 128
        yield (X_batch.reshape(X_batch.shape+(1,)), Y_batch)

# Collect training loss history
history = model.fit_generator(
    image_a_b_gen(batch_size),
    callbacks=[TensorBoard(log_dir="starting_point/Beta-version/output/first_run")],
    epochs=40,
    steps_per_epoch=20
)

# Save model
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")

# Plot training loss
loss = history.history['loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'b', label='Training Loss')
plt.title('Training Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig('mi_grafico.png')

# Test images
Xtest = rgb2lab(1.0/255*X[split:])[:,:,:,0]
Xtest = Xtest.reshape(Xtest.shape+(1,))
Ytest = rgb2lab(1.0/255*X[split:])[:,:,:,1:]
Ytest = Ytest / 128
print(model.evaluate(Xtest, Ytest, batch_size=batch_size))

# Colorize images
color_me = []
for filename in os.listdir('starting_point/Beta-version/Paisajes2/'):
    try:
        img = load_img('starting_point/Beta-version/Paisajes2/' + filename)
        img = img.resize(desired_shape)  # Redimensionar imagen al tamaño deseado
        color_me.append(img_to_array(img))
    except UnidentifiedImageError:
        print(f"Error al cargar la imagen {filename}")

color_me = np.array(color_me, dtype=float)
color_me = rgb2lab(1.0/255*color_me)[:,:,:,0]
color_me = color_me.reshape(color_me.shape+(1,))

# Test model
output = model.predict(color_me)
output = output * 128

# Output colorizations
for i in range(len(output)):
    cur = np.zeros((256, 256, 3))
    cur[:,:,0] = color_me[i][:,:,0]
    cur[:,:,1:] = output[i]
    imsave("starting_point/Beta-version/result/img_"+str(i)+".png", lab2rgb(cur))
