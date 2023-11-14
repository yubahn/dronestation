import os
from django.db import models
from django.utils.translation import gettext_lazy as _


class InputImageModel(models.Model):
    # ImageField 는 원본 이미지를 서버에 저장, 그리고 경로를 DB에 저장
    image = models.ImageField("유저 업로드 이미지", upload_to='yolo_in', blank=True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        
class OutputImageModel(models.Model):
    image = models.ImageField("yolo 결과 이미지", upload_to='yolo_out', blank=True)
    status = models.CharField(max_length=10)
    
class FlightData(models.Model):
    flight = models.IntegerField()
    timestamp = models.IntegerField()
    battery_voltage = models.FloatField(default=0)
    using = 'second_db'
    
    class Meta:
        managed = False  # 모델을 데이터베이스에 생성하지 않도록 설정
        db_table = 'FlightData'