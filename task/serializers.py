from rest_framework import serializers 
from .models import Plant , User, Nursery

class PlantSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,required= False)
    
    class Meta:
        model = Plant
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('name','email','password')