from io import BytesIO
from rest_framework import views, viewsets
from rest_framework.response import Response
from backend.api.models import DentistAdvice, UploadedImage
from .ml.detect import detect, draw_boxes
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from PIL import Image
import numpy as np
from django.core.files.base import ContentFile


from .serializers import (
    DentistAdviceSerializer,
    ProcessedImageSerializer,
    ProcessImageSerializer,
)


index_view = never_cache(TemplateView.as_view(template_name="index.html"))


class ProcessImageView(views.APIView):
    def post(self, request):
        serializer = ProcessImageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            uploaded: UploadedImage = serializer.save()
            pil_image = Image.open(uploaded.image)

            FILENAME, FORMAT = uploaded.image.name, pil_image.format

            # Convert to OpenCV image and detect caries
            open_cv_image = np.array(pil_image)
            boxes, ids, prob = detect(open_cv_image)

            # Prepare to update the ImageField's value
            new_pil_img = Image.fromarray(draw_boxes(open_cv_image, boxes, ids, prob))
            thumb_io = BytesIO()
            new_pil_img.save(thumb_io, FORMAT)

            # Save data
            uploaded.image.save(FILENAME, ContentFile(thumb_io.getvalue()), save=False)
            uploaded.result = {"boxes": boxes, "probabilities": prob}
            uploaded.save()

            # Return created instance as response
            instance = ProcessedImageSerializer(instance=uploaded)
            return Response(instance.data, status=200)


class DentistAdviceViewSet(viewsets.ModelViewSet):
    queryset = DentistAdvice.objects.all()
    serializer_class = DentistAdviceSerializer


class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = ProcessedImageSerializer
    filterset_fields = ["tg_user"]
