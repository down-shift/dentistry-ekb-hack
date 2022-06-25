from rest_framework import serializers
from .models import DentistAdvice, UploadedImage


class DentistAdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DentistAdvice
        fields = "__all__"


class ProcessImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ["tg_user", "image"]


class ProcessedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = "__all__"
