from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets

from .models import Empresa
from .serializers import EmpresaSerializer
# Create your views here.

@api_view(['POST'])
def registrar(request):
	serializer = EmpresaSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)    

@api_view(['GET'])
def empresas(request,pk = None):
    empresa = Empresa.objects.all()
    serializer = EmpresaSerializer(empresa, many=True)
    return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def empresasEdit(request,pk = None):
    if request.method == 'GET':
        empresa = Empresa.objects.filter(id = pk).first()
        serializer = EmpresaSerializer(empresa)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        request.data
        empresa = Empresa.objects.filter(id = pk).first()
        serializer = EmpresaSerializer(empresa, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        empresa = Empresa.objects.filter(id = pk).first()
        empresa.delete()
        return Response('Eliminado')
    
        