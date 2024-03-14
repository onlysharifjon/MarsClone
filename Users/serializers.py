from rest_framework import serializers
from .models import *


# class SutendtLoginSRL(serializers.ModelSerializer):
#     class Meta:
#         model = StudentModel
#         fields = ['modme_id', 'password']


class HammaStudentlarSerializeri(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = "__all__"


class OquvchiIsmi(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ('name',)
