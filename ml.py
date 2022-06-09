import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from statistics import mean
import pickle
import os

#loading the csv data to a pandas dataframe
heart_data=pd.read_csv('heart_disease_data.csv')

#splitting the features and target
X=heart_data.drop(columns="target",axis=1)
Y=heart_data["target"]

#SPLITTING TRAIN AND TEST DATA
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)

# Model Training
#Logistic Regression
model1=LogisticRegression()
model2=KNeighborsClassifier()
model3=DecisionTreeClassifier()
model4=RandomForestClassifier()

#training the LogRegression model with Training data
model1.fit(X_train,Y_train)
model2.fit(X_train,Y_train)
model3.fit(X_train,Y_train)
model4.fit(X_train,Y_train)

Acc_L = dict()
def is_overfit(train_acc,test_acc):
    if train_acc==1 and test_acc <0.85:
        return True
    return False

#Accuracy score FOR Logistic Reg
X_train_prediction1=model1.predict(X_train)
training_data_accuracy1=accuracy_score(X_train_prediction1,Y_train)
X_test_prediction1=model1.predict(X_test)
testing_data_accuracy1=accuracy_score(X_test_prediction1,Y_test)
if not is_overfit(training_data_accuracy1,testing_data_accuracy1):
    Acc_L["model1"] = mean([training_data_accuracy1,testing_data_accuracy1])

# for KNN
X_train_prediction2=model2.predict(X_train)
training_data_accuracy2=accuracy_score(X_train_prediction2,Y_train)
X_test_prediction2=model2.predict(X_test)
testing_data_accuracy2=accuracy_score(X_test_prediction2,Y_test)
if not is_overfit(training_data_accuracy2,testing_data_accuracy2):
    Acc_L["model2"] = mean([training_data_accuracy2,testing_data_accuracy2])

# For decision trees
X_train_prediction3=model3.predict(X_train)
training_data_accuracy3=accuracy_score(X_train_prediction3,Y_train)
X_test_prediction3=model3.predict(X_test)
testing_data_accuracy3=accuracy_score(X_test_prediction3,Y_test)
if not is_overfit(training_data_accuracy3,testing_data_accuracy3):
    Acc_L["model3"] = mean([training_data_accuracy3,testing_data_accuracy3])

# for Random Forest
X_train_prediction4=model4.predict(X_train)
training_data_accuracy4=accuracy_score(X_train_prediction4,Y_train)
X_test_prediction4=model4.predict(X_test)
testing_data_accuracy4=accuracy_score(X_test_prediction4,Y_test)
if not is_overfit(training_data_accuracy4,testing_data_accuracy4):
    Acc_L["model4"] = mean([training_data_accuracy4,testing_data_accuracy4])

max_acc = 0
classifier = None
for k,v in Acc_L.items():
    if max_acc < v:
        max_acc = v
        if k == "model1":
            classifier = model1
        elif k == "model2":
            classifier = model2
        elif k == "model3":
            classifier = model3
        elif k == "model4":
            classifier = model4

print(classifier)
save_path = 'prediction/'
completeName = os.path.join(save_path, "heartml.pkl")         
pickle.dump(classifier, open(completeName, 'wb'))