from  rest_framework import  serializers
from .models import *

class SutendtLoginSRL(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['modme_id', 'password']


