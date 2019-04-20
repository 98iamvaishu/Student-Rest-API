from main.models import *
from rest_framework import viewsets, routers
from .serializers import *
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout


class Signup(viewsets.ModelViewSet):

	def signup(request):
		is_staff = False
		is_admin = False
		if request.method == "POST":
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			organization = request.POST['organization']
			email = request.POST['email']
			password = request.POST['password']
			designation = request.POST['designation']
			user = authenticate(request, email=email, password=password)

			if user is None:
				user = UserModel.objects.create_user(email,password)
				signup = Signup.objects.create(user=user,first_name = first_name,last_name=last_name,organization=organization,designation=designation)
				login(request, user)
				return HttpResponse("New user createed")
			else:
				return HttpRespose("Already exists")
		return render(request, "signup.html")
	queryset = Signup.objects.all()
	serializer_class = SignupSerializer


class Signin(viewsets.ModelViewSet):
	def signin(self,request):
		if request.method == "POST":
			email=request.POST['email']
			password=request.POST['password']
			user=authenticate(request, email=email, password=password)
			print(user)
			if user is not None:
				login(request, user)
				return HttpResponse("Succssfully logged in ")
			else:
				return HttpResponse("user not found")
		return render(request, "signin.html")
	queryset = UserModel.objects.all()
	serializer_class = SigninSerializer
