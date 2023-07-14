from django.shortcuts import render,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from crud.models import *
from .serializers import *

from django.http.response import JsonResponse


@api_view(['GET','POST','DELETE'])
def specialization_list(request):
    if request.method == 'GET':
        especialidades = Specialization.objects.all()
        especialidades_serializer = SpecializationSerializer(especialidades,many=True)
        return Response(especialidades_serializer.data)

    elif request.method == 'POST':
        especialidad_data = JSONParser().parse(request)
        especialidades_serializer = SpecializationSerializer(data=especialidad_data)
        if especialidades_serializer.is_valid():
            especialidades_serializer.save()
            return JsonResponse(especialidades_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(especialidades_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cantidad = Specialization.objects.all().delete()
        return Response({'mensajes':'Se han eliminado {} especialidades de la base de datos'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def specialization_detail(request,id):
    try:
        especialidad = Specialization.objects.get(id=id)
    except:
        return Response({'mensaje':'La especialidad {} no existen en nuestros registros'.format(id)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        especialidad_serializer = SpecializationSerializer(especialidad)
        return Response(especialidad_serializer.data)
    ## METODO POST SIRVE CON ESPECIALIDADES
    elif request.method == 'PUT':
        especialidad_data = JSONParser().parse(request)
        especialidades_serializer = SpecializationSerializer(especialidad, data=especialidad_data)
        if especialidades_serializer.is_valid():
            especialidades_serializer.save()
            return JsonResponse(especialidades_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(especialidades_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        especialidad.delete()
        return Response({'mensaje':'La especialidad {} ha sido eliminada de la base de datos.'.format(id)},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def subject_list(request):
    if request.method == 'GET':
        asignaturas = Subject.objects.all()

        subject = request.query_params.get('subject',None)
        if subject is not None:
            asignaturas = asignaturas.filter(subject__contains=subject)

        semester = request.query_params.get('semester',None)
        if semester is not None:
            asignaturas = asignaturas.filter(semester__contains=semester)

        specialization = request.query_params.get('specialization',None)
        if specialization is not None:
            asignaturas = asignaturas.filter(specialization__specialization__contains=specialization)

    
        asignaturas_serializer = SubjectSerializer(asignaturas,many=True)
        return Response(asignaturas_serializer.data)

    elif request.method == 'POST':
        asignatura_data = JSONParser().parse(request)
        aignaturas_serializer = SubjectSerializer(data=asignatura_data)
        if aignaturas_serializer.is_valid():
            aignaturas_serializer.save()
            return JsonResponse(aignaturas_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(aignaturas_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


## metodo que sirivio
##if request.method == 'GET':
##        especialidades = Specialization.objects.all()
##        especialidades_serializer = SpecializationSerializer(especialidades,many=True)
##        return Response(especialidades_serializer.data
