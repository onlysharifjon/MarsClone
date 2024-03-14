from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import HammaStudentlarSerializeri,OquvchiIsmi
from rest_framework.response import Response
# Create your views here.

class AllStudents(APIView):
    def get(self,request):
        oquvchilar = StudentModel.objects.all()
        serializer = HammaStudentlarSerializeri(oquvchilar,many=True)
        return Response(serializer.data)


class BittaOquvchi(APIView):
    serializer_class = OquvchiIsmi

    def post(self,request):
        ismi = request.data.get('name')
        oquvchi = StudentModel.objects.all().filter(name = ismi)

        if oquvchi:
            serializer = HammaStudentlarSerializeri(oquvchi, many=True)
            return Response(serializer.data)
        else:
            return Response({'Message': "User Not Found"})



