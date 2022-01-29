from dataclasses import dataclass
import pandas 
from sklearn.model_selection import train_test_split  
import tensorflow as tf

breastCancerDataSet = pandas.read_csv('data.csv')

x = breastCancerDataSet.drop(columns=["diagnosis(1=m, 0=b)"])  
y = breastCancerDataSet["diagnosis(1=m, 0=b)"]
trainX, testX, trainY, testY = train_test_split(x, y, test_size=0.2) 
model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(128, input_shape=trainX.shape[1:], activation="sigmoid"))
model.add(tf.keras.layers.Dense(128, activation="sigmoid"))
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))  
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(trainX, trainY, epochs=1000)
model.evaluate(testX, testY)
