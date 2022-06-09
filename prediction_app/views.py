from rest_framework.views import APIView
from .serializers import HeartDiseaseSerializer
from rest_framework import status
from rest_framework.response import Response
import pandas as pd
import joblib
from django.shortcuts import render 
import tensorflow as tf
import numpy as np

def HomeView(request):
    return render(request,'home.html')

def heartmlview(request):
    return render(request,'predict.html')

def heartannview(request):
    return render(request,'predict_ann.html')

# Create your views here.
class HeartMachineLearningAPIView(APIView):
    """
    
    Machine Learning API View
    
    """    
    def post(self,request, *args, **kwargs):
        
        data = self.request.data
        if "sex" in data:
            if data["sex"]=="M":
                data["sex"] = 1
            elif data["sex"]=="F":
                data["sex"] = 0
        serializer = HeartDiseaseSerializer(data=data,partial=True)
        if serializer.is_valid():
            instance = serializer.save()
    
            data=list(data.values())        
            df_data=pd.DataFrame([data],columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg','thalach','exang','oldpeak','slope','ca','thal'])      
                
            final_model=joblib.load("prediction/heartml.pkl")
            # pickle.load
            y_pred = final_model.predict(df_data)[0]
            print(y_pred)

            if(y_pred==1):
                str_res='There is a chance of heart failure in the feature.'
            else:
                str_res='No chance of getting heart failure as of now'
            instance.target=y_pred
            instance.save()
            return Response(data = {'result':str_res} ,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

class HeartANNAPIView(APIView):
    """
    
    ANN APIView
    
    """    
    def post(self,request, *args, **kwargs):
        
        data = self.request.data
        if "sex" in data:
            if data["sex"]=="M":
                data["sex"] = 1
            elif data["sex"]=="F":
                data["sex"] = 0
        serializer = HeartDiseaseSerializer(data=data,partial=True)
        if serializer.is_valid():
            instance = serializer.save()
    
            data=list(data.values())        
            data = np.asarray(data).astype(np.float32)
            df_data=pd.DataFrame([data],columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg','thalach','exang','oldpeak','slope','ca','thal'])      
                
            final_model=tf.keras.models.load_model("prediction/heartann")
            # final_model=joblib.load("prediction/heartann.pkl")
            y_pred = final_model.predict(df_data)[0]
            print(y_pred)

            if(y_pred==1):
                str_res='There is a chance of heart failure in the feature.'
            else:
                str_res='No chance of getting heart failure as of now'
            instance.target=y_pred
            instance.save()
            return Response(data = {'result':str_res} ,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)