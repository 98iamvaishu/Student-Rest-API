from rest_framework import serializers
from main.models import *



class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('roll_no', 'name', 'age',
                  'standard')

