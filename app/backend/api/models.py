from django.db import models
from rest_framework import serializers


# class TelegramUser(models.Model):
#     telegram_id = models.IntegerField("Telegram ID")
#     chat_id = models.IntegerField("Telegram chat ID")


# class TelegramUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TelegramUser
#         fields = "__all__"


class UploadedImage(models.Model):
    image = models.ImageField("Изображение")
    result = models.JSONField("Обработанное изображение", default=dict)
