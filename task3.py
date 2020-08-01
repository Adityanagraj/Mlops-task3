# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.datasets import mnist
from keras.utils import np_utils
from keras.optimizers import Adam

(xtrain, ytrain), (xtest, ytest)  = mnist.load_data()

img_rows = xtrain[0].shape[0]
img_cols = xtrain[1].shape[0]

# Our original image shape of (60000,28,28) to (60000,28,28,1)
xtrain = xtrain.reshape(xtrain.shape[0], img_rows, img_cols, 1)
xtest = xtest.reshape(xtest.shape[0], img_rows, img_cols, 1)

input_shape = (img_rows, img_cols, 1)

#changing our image datatype
xtrain = xtrain.astype('float32')
xtest = xtest.astype('float32')

#conversion of cathegorical variable 
ytrain = np_utils.to_categorical(ytrain)
ytest = np_utils.to_categorical(ytest)

num_classes = ytest.shape[1]

model=Sequential()

model.add(Conv2D(30, (5, 5),
                 padding = "same", 
                 input_shape = input_shape))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Flatten())
model.add(Dense(units=20, activation='relu'))

model.add(Dense(num_classes))
model.add(Activation("softmax"))

model.compile(loss = 'categorical_crossentropy', optimizer = Adam(), metrics = ['accuracy'])

print(model.summary())

batch_size = 124
epochs = 1

history = model.fit(xtrain, ytrain, batch_size=batch_size, epochs=epochs, validation_data=(xtest, ytest), shuffle=True)

scores = model.evaluate(xtest, ytest, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

print(scores[1])

file = open('data.txt', 'w')
file.write(str(int(scores[1])))

