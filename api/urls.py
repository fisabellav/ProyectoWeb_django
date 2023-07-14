from django.urls import path
from .views import *

urlpatterns = [
    path('especialidades/', specialization_list),
    path('especialidades/<int:id>/', specialization_detail),
    path('asignaturas/', subject_list),
]