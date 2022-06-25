from rest_framework import views, serializers
from rest_framework.response import Response
from backend.api.models import UploadedImage
from .ml.detect import pag
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from PIL import Image
import numpy as np


index_view = never_cache(TemplateView.as_view(template_name="index.html"))


class ProcessImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ("image",)


class ProcessedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = "__all__"


class ProcessImageView(views.APIView):
    def post(self, request):
        serializer = ProcessImageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            uploaded: UploadedImage = serializer.save()
            pil_image = Image.open(uploaded.image).convert("RGB")
            open_cv_image = np.array(pil_image)
            boxes, prob = pag(open_cv_image)
            result = {"boxes": boxes, "probabilities": prob}
            uploaded.result = result
            uploaded.save()

            instance = ProcessedImageSerializer(instance=uploaded)
            return Response(instance.data, status=200)


# class TelegramUserViewSet(viewsets.ModelViewSet):
#     queryset = TelegramUser.objects.all()
#     serializer_class = TelegramUserSerializer
