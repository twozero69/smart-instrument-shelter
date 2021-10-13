#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import *
from api.serializers import *


# Create your views here.
@csrf_exempt
def datas1_list(request):
	if request.method=='GET':
		query_set=datas1.objects.all()
		serializer=datas1_serializer(query_set, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method=='POST':
		data=JSONParser().parse(request)

		########################
		
		########################

		serializer=datas1_serializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def datas1_one(request):
	if request.method=='GET':
		query_set=datas1.objects.last()
		serializer=datas1_serializer(query_set)
		return JsonResponse(serializer.data, safe=False)





@csrf_exempt
def datas2_list(request):
	if request.method=='GET':
		query_set=datas2.objects.all()
		serializer=datas2_serializer(query_set, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method=='POST':
		data=JSONParser().parse(request)

		########################
		
		########################

		serializer=datas2_serializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def datas2_one(request):
	if request.method=='GET':
		query_set=datas2.objects.last()
		serializer=datas2_serializer(query_set)
		return JsonResponse(serializer.data, safe=False)
		
		
		
		
		
@csrf_exempt
def datas3_list(request):
	if request.method=='GET':
		query_set=datas3.objects.all()
		serializer=datas3_serializer(query_set, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method=='POST':
		data=JSONParser().parse(request)

		########################
		
		########################

		serializer=datas3_serializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def datas3_one(request):
	if request.method=='GET':
		query_set=datas3.objects.last()
		serializer=datas3_serializer(query_set)
		return JsonResponse(serializer.data, safe=False)


