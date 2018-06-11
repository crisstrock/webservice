# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from usuarios.models import User, Carrera
from usuarios.serializers import UsuarioSerializer, CarreraSerializer

# Create your views here.
#------------------------Usuarios----------------------------------
@csrf_exempt
def usuario_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        usuarios = User.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def usuario_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        usuario = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        usuario.delete()
        return HttpResponse(status=204)

#---------------CArrera------------------------------------

@csrf_exempt
def carrera_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        carreras = Carrera.objects.all()
        serializer = CarreraSerializer(carreras, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarreraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def carrera_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        carrera = Carrera.objects.get(pk=pk)
    except Carrera.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarreraSerializer(carrera)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarreraSerializer(carrera, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        carrera.delete()
        return HttpResponse(status=204)

def lista_carrera(request):
    carreras = Carrera.objects.all()
    return render_to_response('templates/tabla.html',{'carreras':carreras})