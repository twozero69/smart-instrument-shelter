from rest_framework import serializers
from .models import datas1, datas2, datas3

class datas1_serializer(serializers.ModelSerializer):
	class Meta:
		model=datas1
		fields=['temperature', 'humidity', 'windspeed', 'rain', 'pressure', 'altitude', 'vibration', 'timestamp']
		


class datas2_serializer(serializers.ModelSerializer):
	class Meta:
		model=datas2
		fields=['latitude', 'longitude', 'timestamp']
		
		
		
class datas3_serializer(serializers.ModelSerializer):
	class Meta:
		model=datas3
		fields=['precipitation', 'cloud', 'thunderdist', 'timestamp']
