from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework import routers

from .api.views import (
    index_view,
    ProcessImageView,
    UploadedImagesViewSet,
    DentistAdviceViewSet,
)

router = routers.DefaultRouter()
router.register("advice", DentistAdviceViewSet)
router.register("uploads", UploadedImagesViewSet)

urlpatterns = [
    path("", index_view, name="index"),
    path("api/", include(router.urls)),
    path("api/admin/", admin.site.urls),
    path("api/detect/", ProcessImageView.as_view(), name="detect"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
