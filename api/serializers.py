from rest_framework import serializers
from .models import ImageData

class ImageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageData
        fields = '__all__'


        # serializers.py

class ImageDataSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ImageData
        fields = '__all__'