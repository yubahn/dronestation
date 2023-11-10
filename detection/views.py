import cv2
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import InputImageModel, OutputImageModel
from django.shortcuts import render
import io
from PIL import Image as im
import torch
import base64
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime

current_datetime = datetime.now()
file_name_index = 0

class Index(APIView):
    def get(self, request):
        return render(request, 'detection/index.html')

class DetectionWeb(APIView):
    def get(self, request):
        return render(request, 'detection/index1.html')
    
    def post(self, request):
        # 사용자가 업로드한 이미지 원본 서버 저장 및 서버 경로를 DB에 저장
        upload_img = request.FILES.get('image')
        img_instance = InputImageModel(image = upload_img)
        img_instance.save()
        
        # 저장된 원본 이미지를 byte 형식으로 읽음
        uploaded_img = InputImageModel.objects.filter().last()
        img_bytes = uploaded_img.image.read()
        img = im.open(io.BytesIO(img_bytes))
        
        # yolov5 detection
        path_hubconfig = "yolov5"
        path_weightfile = "yolov5/weight/yolov5s.pt"  # or any custom trained model

        model = torch.hub.load(path_hubconfig, 'custom',    # 'custom' 가능
                            path=path_weightfile, source='local')

        results = model(img, size=640)
        
        results.render()
        
        # yolo 결과 jpg 형식 media 루트에 저장
        for img in results.ims:
            img_base64 = im.fromarray(img)
            img_base64.save(f"media/yolo_out/{upload_img}", format="JPEG")
        
        # yolo 결과 db에 저장
        inference_img = f"media/yolo_out/{upload_img}"
        result_img = OutputImageModel(image = inference_img)
        result_img.save()
        
        # 바이너리로 전달을 위한 저장
        with open(inference_img, 'rb') as image_file:
            image_bytes = image_file.read()
            
        #image_bytes 를 전달해주면 됨
        response_data = {
            'image': inference_img
        }
        
        print(response_data)
        return render(request, "detection/index1.html", {'response_data': f'/response_data'})

class DetectionAPI(APIView):
    def get(self, request):
        return render(request, 'detection/index1.html')
    
    def post(self, request):
        global file_name_index
        upload_img = request.data['image']
        
        file_name = f"dronestation_{current_datetime.strftime('%Y-%m-%d')}_{file_name_index}.jpg"
        img = im.open(io.BytesIO(base64.b64decode(upload_img)))

        image_tmp = io.BytesIO()
        img.save(image_tmp, 'JPEG')
        image_file = SimpleUploadedFile(f"{file_name}", image_tmp.getvalue())
        
        # 사용자가 업로드한 이미지 원본 서버 저장 및 서버 경로를 DB에 저장 
        img_instance = InputImageModel(image = image_file)
        img_instance.save()
        
        # 저장된 원본 이미지를 byte 형식으로 읽음
        uploaded_img = InputImageModel.objects.filter().last()
        img_bytes = uploaded_img.image.read()
        img = im.open(io.BytesIO(img_bytes))
        
        # 잘라낼 부분의 좌표 
        width, height = img.size
        left = 600
        top = height - 1000
        right = 4000
        bottom = height

        # 이미지 자르기
        cropped_image = img.crop((left, top, right, bottom))
        
        # yolov5 detection
        path_hubconfig = "yolov5"
        path_weightfile = "yolov5/weight/propeller_ep1000.pt"  

        # 저장소, 모델 or 모듈, 가중치 파일, 다운로드 위치
        #torch.hub.load(저장소 패스, 모델 패스, 가중치 패스, gitgub or local)
        model = torch.hub.load(path_hubconfig, 'custom',
                            path=path_weightfile, source='local')
        
        results = model(cropped_image, size=640)
        
        results.render()
        
        # yolo 결과 jpg 형식 media 루트에 저장
        for img in results.ims:
            img_base64 = im.fromarray(img)
            img_base64.save(f"media/yolo_out/{file_name}", format="JPEG")
        
        # yolo 결과 db에 저장
        inference_img = f"media/yolo_out/{file_name}"
        result_img = OutputImageModel(image = inference_img)
        result_img.save()
        
        # 바이너리로 전달을 위한 저장
        with open(inference_img, 'rb') as image_file:
            image_bytes = image_file.read()
            
        result = base64.b64encode(image_bytes)
        
        result_data = {
            "result": result.decode('utf-8')
        }
        file_name_index += 1

        return JsonResponse(result_data)
    