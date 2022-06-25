from django.db import models
from datetime import datetime


class UploadedImage(models.Model):
    image = models.ImageField("Изображение")
    result = models.JSONField("Обработанное изображение", default=dict)
    tg_user = models.IntegerField("Пользователь", default=None, null=True)
    gen_time = models.DateTimeField("Время обработки", auto_now_add=True)
    filename = models.CharField(max_length=255, default="")

    class Meta:
        ordering = ["-gen_time"]


class DentistAdvice(models.Model):
    text = models.TextField()
