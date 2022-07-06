# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 17:09:09 2022

@author: amacemirhan
"""

from tensorflow import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import cv2
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
print(tf.__version__)





DATADIR = "C:/PythonKodlar/YSAPROJE/Oklarv2"
CATEGORIES = ["L", "R" , "up"]

for category in CATEGORIES:
  path = os.path.join(DATADIR, category) # path to right,up and left arrows dir
  for img in os.listdir(path):
    img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
    plt.imshow(img_array, cmap="gray")
    plt.show()
    break
  break

#Batch - Size - Width
batch_size = 32
img_height = 480
img_width = 640


#Train And Validation
train_ds = tf.keras.utils.image_dataset_from_directory(
  DATADIR,
  validation_split=0.3,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
  DATADIR,
  validation_split=0.3,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

class_names = train_ds.class_names
print(class_names)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")

for image_batch, labels_batch in train_ds:
  print(image_batch.shape)
  print(labels_batch.shape)             
  break

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

normalization_layer = layers.Rescaling(1./255)

normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
# Pixel değerleri [0,1] aralığında !
print(np.min(first_image), np.max(first_image))

num_classes = len(class_names)



#Model
model = Sequential([
  layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

"""
#Eğitim
epochs=3
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
        
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
"""

#Tahmin
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input

image = load_img('C:/PythonKodlar/YSAPROJE/L (2).png', target_size=(480, 640))
# convert the image pixels to a numpy array
image = img_to_array(image)
# reshape data for the model
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# prepare the image for the VGG model
image = preprocess_input(image)
# predict the probability across all output classes


print(model.predict(image))

from keras.preprocessing.image import load_img

def testedici(TestImages):
  for i in range(125):
    try:
      pathx = TestImages + "("+ str(i+1) +").png"

      image = load_img(pathx, target_size=(480, 640))
      image = img_to_array(image)
      image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
      image = preprocess_input(image)
      #print(pathx)
      array2dir(model.predict(image))
      #print(model.predict(image))
    except:
      1==1
def array2dir(array):
    if array[0][0] > array[0][1] and array[0][0] > array[0][2]:
            print("sol")

    if array[0][1] > array[0][0] and array[0][1] > array[0][2]:
            print("sağ")

    if array[0][2] > array[0][1] and array[0][2] > array[0][0]:
            print("yukarı")



"""
TestPath = "/content/drive/MyDrive/Ysa Proje/TestData/test"
TestSol = TestPath+"/L/L "
TestYukari = TestPath+"/U/U "
TestSag = TestPath+"/R/R "
print("\nSol Oklar")
testedici(TestSol)
print("\nYukari Oklar")
testedici(TestYukari)
print("\nSag Oklar")
testedici(TestSag)
"""

import time



"""
i=0
while i<10:
    i+=1
    SS = pyautogui.screenshot('SS.png')
    image = load_img(("C:/PythonKodlar/YSAPROJE/SS.png"), target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    #print(pathx)
    x=model.predict(image)
    array2dir(x)
    print(x)
    time.sleep(0.5)
    print(i)
 """  
 
#keras.models.save_model('C:/PythonKodlar/YSAPROJE/model2')
model = keras.models.load_model('C:/PythonKodlar/YSAPROJE/model')



def take_photo():
    vid = cv2.VideoCapture(0)
  
    while(True):
          
        # Capture the video frame
        # by frame
        ret, image = vid.read()
      
        # Display the resulting frame
        cv2.imshow('Kamera', image)
          
        
        
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        image = preprocess_input(image)
        x=model.predict(image)
        array2dir(x)
        print(x)
        time.sleep(0.2)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
      
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


from IPython.display import Image
try:
  filename = take_photo()
  print('Saved to {}'.format(filename))
  
  # Show the image which was just taken.
  display(Image(filename))
except Exception as err:

  # Errors will be thrown if the user does not have a webcam or if they do not
  # grant the page permission to access it.
  print(str(err))





image = load_img(("C:/PythonKodlar/YSAPROJE/SS.png"), target_size=(480, 640))
image = img_to_array(image)
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
image = preprocess_input(image)
#print(pathx)
x=model.predict(image)
array2dir(x)
print(x)

TestDataDIR = "C:\PythonKodlar\YSAPROJE\TestData\TestData"

CATEGORIES = ["L", "R" , "U"]

for category in CATEGORIES:
  path = os.path.join(TestDataDIR, category) # path to right,up and left arrows dir
  for img in os.listdir(path):
    img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
    plt.imshow(img_array, cmap="gray")
    plt.show()
    break
  break


test_data=[]
IMG_SIZE=224
def create_test_data():
  for category in CATEGORIES:
    path = os.path.join(TestDataDIR, category) # path to right,up and left arrows dir
    class_num = CATEGORIES.index(category)
    for img in os.listdir(path):
      try:
        img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_COLOR)
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        test_data.append([new_array, class_num])
      except Exception as e:
        pass
create_test_data()
print(len(test_data))


