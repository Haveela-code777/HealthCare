from rest_framework import serializers
from .models import HeartDisease

class HeartDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartDisease
        fields = "__all__"
