from main.models import *
from rest_framework import viewsets, routers
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout

@api_view(['GET','POST'])
def Studentlist(request):
	if request.method == 'GET':
		posts = Student.objects.all()
		serializer = StudentSerializer(posts, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
