from django.urls import path, include
from .views import Index, DetectionWeb, DaDetectionAPI, FdDetectionAPI


urlpatterns = [
    path("main/", Index.as_view()),
    path("detectionweb/", DetectionWeb.as_view()),
    path("imgdetectionapi/", DaDetectionAPI.as_view()),
    path("fddetectionapi/", FdDetectionAPI.as_view())
]