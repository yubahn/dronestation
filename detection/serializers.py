from rest_framework import serializers
from .models import InputImageModel, OutputImageModel

class InputImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(help_text='InputImage')
    
    class Meta:
        model = InputImageModel
        fields = "__all__"
        
class OutputImageSerializer(serializers.ModelSerializer):
    image = serializers.CharField(help_text='OutputImage')
    
    class Meta:
        model = OutputImageModel
        fields = "__all__"