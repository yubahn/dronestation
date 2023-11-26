from django.urls import path, include
from .views import Index, DetectionWeb, ImgDetectionAPI, FdDetectionAPI


urlpatterns = [
    path("main/", Index.as_view()),
    path("detectionweb/", DetectionWeb.as_view()),
    path("imgdetectionapi/", ImgDetectionAPI.as_view()),
    path("fddetectionapi/", FdDetectionAPI.as_view())
]