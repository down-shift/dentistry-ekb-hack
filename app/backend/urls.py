from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from .api.views import index_view, ProcessImageView

router = routers.DefaultRouter()
# router.register("users", TelegramUserViewSet)

urlpatterns = [
    path("", index_view, name="index"),
    path("api/admin/", admin.site.urls),
    # path("api/", include(router.urls)),
    path("api/detect/", ProcessImageView.as_view(), name="detect"),
]
