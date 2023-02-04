from django.shortcuts import render
from app.models import employee
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.serializer import employeeserializer


# Create your views here.
@api_view(['GET'])
def home(request):
    emp=employee.objects.all()
    serializer=employeeserializer(emp,many=True)
    return Response(serializer.data)
