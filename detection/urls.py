from django.urls import path, include
from .views import Index, DetectionWeb, DetectionAPI


urlpatterns = [
    path("main/", Index.as_view()),
    path("detectionweb/", DetectionWeb.as_view()),
    path("detectionapi/", DetectionAPI.as_view()),
]
