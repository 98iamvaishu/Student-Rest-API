from rest_framework import serializers
from main.models import *



class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Signup
        fields = ('first_name', 'last_name', 'organization',
                  'email', 'password', 'designation')


class SigninSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('email', 'password')
