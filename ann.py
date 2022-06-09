import pandas as pd
import tensorflow as tf
# from keras.models import Sequential
# from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os
# import pickle

data = pd.read_csv('heart_disease_data.csv')

#splitting the features and target
X=data.drop(columns="target",axis=1)
Y=data["target"]

X_train,X_test,y_train, y_test = train_test_split(X,Y,test_size = 0.3 , random_state = 0 )

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = tf.keras.Sequential()
classifier.add(tf.keras.layers.Dense(activation = "relu", input_dim = 13,units = 8, kernel_initializer = "uniform"))
classifier.add(tf.keras.layers.Dense(activation = "relu", units = 14,kernel_initializer = "uniform"))
classifier.add(tf.keras.layers.Dense(activation = "sigmoid", units = 1,kernel_initializer = "uniform"))
classifier.compile(optimizer = 'adam' , loss = 'binary_crossentropy',metrics = ['accuracy'] )

classifier.fit(X_train , y_train , batch_size = 8 ,epochs = 100 )

# save_path = 'prediction/'
# completeName = os.path.join(save_path, "heartann.h5") 
# pickle.dump(classifier, open(completeName, 'wb'))
classifier.save('prediction/heartann')