from django.db import models

# Create your models here.
class datas1(models.Model):
	temperature=models.FloatField()
	humidity=models.FloatField()
	windspeed=models.FloatField()
	rain=models.FloatField()
	pressure=models.FloatField()
	altitude=models.FloatField()
	vibration=models.BooleanField()

	timestamp=models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=['timestamp']
		

class datas2(models.Model):
	latitude=models.FloatField()
	longitude=models.FloatField()
	
	timestamp=models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=['timestamp']
		

class datas3(models.Model):
	precipitation=models.FloatField()
	cloud=models.FloatField()
	thunderdist=models.FloatField()
	
	timestamp=models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=['timestamp']
