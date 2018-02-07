import json
from keras.models import model_from_json
import numpy as np

X = np.asmatrix([0.49405947, 0.50894321, 0.52537861, 0.50926956, 0.51894845, 0.49075743, 0.48602009, 0.50945465], dtype = np.float) ## This is our test vector

print(X.shape)

## https://machinelearningmastery.com/save-load-keras-deep-learning-models/

# load json and create model
json_file = open('model.nn', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

print(X.shape)
print(type(X))
print(type(X[0]))
print(X[0][0])

predictions = loaded_model.predict(X)

print(predictions)
