from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('especialidades/', especialidades, name='especialidades'),
    path('especialidades/asignaturas/', asignaturas, name='asignaturas'),
    path('especialidades/asignaturas/<specialization>', subjects_by_specialization, name='asignaturas-especialidad'),
    path('especialidades/asignaturas/apuntes/', apuntes, name='apuntes'),
    path('especialidades/asignaturas/apuntes/<subject>', notes_by_subject, name='apuntes-asignatura'),
    path('contacto/', contacto, name='contacto'),
    path('nosotros/', nosotros, name='nosotros'),
    path('recursos/', recursos, name='recursos'),
]