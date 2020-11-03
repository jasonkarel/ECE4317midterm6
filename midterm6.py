# -*- coding: utf-8 -*-
"""Midterm6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XlnFMLdjMKK35dNphKi-Rl6ogZxtvJro
"""

# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)



fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0

test_images = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

accuracy_arr = []
test_set_amount_array = []
i = 0;
x = 2
for x in range(100, 3000, 100):
  model.fit(train_images[1:x], train_labels[1:x], epochs=10)
  test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
  test_set_amount_array.append(x)
  accuracy_arr.append(test_acc)
  i +=1
  print('\nTest accuracy:', test_acc)

print(accuracy_arr)
print(test_set_amount_array)

plt.plot(test_set_amount_array, accuracy_arr)
plt.xlabel("Training Set Size")
plt.ylabel("Proportion Correct on Test Set")

plt.show()