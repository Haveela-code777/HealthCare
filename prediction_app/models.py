from django.db import models

# Create your models here.

class HeartDisease(models.Model):
    age = models.IntegerField(null=True, blank=True)
    sex = models.IntegerField(null=True, blank=True)
    cp = models.IntegerField(null=True, blank=True)
    trestbps = models.IntegerField(null=True, blank=True)
    chol = models.IntegerField(null=True, blank=True)
    fbs = models.IntegerField(null=True, blank=True)
    restecg= models.IntegerField(null=True, blank=True)
    thalach= models.IntegerField(null=True, blank=True)
    exang= models.IntegerField(null=True, blank=True)
    oldpeak= models.FloatField(null=True, blank=True)
    slope= models.IntegerField(null=True, blank=True)
    ca= models.IntegerField(null=True, blank=True)
    thal= models.IntegerField(null=True, blank=True)
    target= models.IntegerField(null=True, blank=True)