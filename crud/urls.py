from django.urls import path
from .views import *

urlpatterns = [
    path('especialidades/', especialidades_crud, name="especialidades-crud"),
    path('especialidades/specialization_new', specialization_new, name="specialization-new"),
    path('especialidades/edit/<id>', specialization_edit, name="specialization-edit"),
    path('especialidades/detail/<id>', specialization_detail, name="specialization-detail"),
    path('especialidades/delete/<id>', specialization_delete, name="specialization-delete"),
    path('asignaturas/', asignaturas_crud, name='asignaturas-crud'),
    path('asignaturas/subject_new', subject_new, name="subject-new"),
    path('asignaturas/edit/<id>', subject_edit, name="subject-edit"),
    path('asignaturas/detail/<id>', subject_detail, name="subject-detail"),
    path('asignaturas/delete/<id>', subject_delete, name="subject-delete"),
    path('asignaturas/<specialization>', subjects_by_specialization_crud, name='asig-especialidad-crud'),
    path('apuntes/', apuntes_crud, name='apuntes-crud'),
    path('apuntes/apuntes_new', note_new, name='note-new'),
    path('apuntes/edit/<idNote>', note_edit, name='note-edit'),
    path('apuntes/detail/<idNote>', note_detail, name='note-detail'),
    path('apuntes/delete/<idNote>', note_delete, name='note-delete'),
]