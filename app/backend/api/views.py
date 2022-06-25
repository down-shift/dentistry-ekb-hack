from distutils.command.upload import upload
from io import BytesIO
from rest_framework import views, serializers
from rest_framework.response import Response
from backend.api.models import UploadedImage
from .ml.detect import detect, draw_boxes
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import numpy as np
from django.core.files.base import ContentFile

from os.path import splitext


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
            pil_image = Image.open(uploaded.image)
            open_cv_image = np.array(pil_image)
            boxes, ids, prob = detect(open_cv_image)
            result = {"boxes": boxes, "probabilities": prob}
            uploaded.result = result
            uploaded.save()

            FILENAME = uploaded.image.name

            new_pil_img = Image.fromarray(draw_boxes(open_cv_image, boxes, ids, prob))

            thumb_io = BytesIO()
            new_pil_img.save(thumb_io, pil_image.format)
            uploaded.image.save(FILENAME, ContentFile(thumb_io.getvalue()), save=False)
            uploaded.save()
            instance = ProcessedImageSerializer(instance=uploaded)
            return Response(instance.data, status=200)


# class TelegramUserViewSet(viewsets.ModelViewSet):
#     queryset = TelegramUser.objects.all()
#     serializer_class = TelegramUserSerializer
