'''Function which loads a model with the provided json file with
the model description and a .h5 file containing the weights.
'''

from __future__ import print_function
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.models import model_from_json
import numpy as np
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import np_utils
import load2

def load_trained_model():
	batch_size = 32
	nb_classes = 6
	nb_epoch = 1
	data_augmentation = True

	# input image dimensions
	img_rows, img_cols = 160, 210
	# the CIFAR10 images are RGB
	img_channels = 3

	# the data, shuffled and split between train and test sets
	(X_train, y_train), (X_test, y_test) = load2.load_data()
	#print(X_train[:100])
	#print(y_train[:100])
	X_pred = X_test[:500]
	#X_pred = np.reshape(X_pred, (1, 3, 160, 210))
	print(X_pred.shape)
	print(X_pred.size)
	print(X_pred)
	print(y_test[:500])
	#x_predict = np.reshape(x_pred, (1000, 3, 160, 210))
	print('X_train shape:', X_train.shape)
	print(X_train.shape[0], 'train samples')
	print(X_test.shape[0], 'test samples')
	print(y_test.shape, 'y test'
	)
	# load json and create model
	json_file = open('model2.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)

	# load weights into new model
	loaded_model.load_weights("model2.h5")
	print("Loaded model from disk")
	sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
	loaded_model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

	return loaded_model

