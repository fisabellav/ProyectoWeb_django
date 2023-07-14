from django import forms
from django.forms import ModelForm
from .models import *

class SpecializationForm(ModelForm):
    class Meta:
        model = Specialization
        fields = [
            'specialization',
            'image'
        ]
        labels = {
            'specialization':'Especialidad',
            'image':'Imagen'
        }
        widgets = {
            'specialization':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = [
            'subject',
            'specialization',
            'semester',
            'image'
        ]
        labels = {
            'subject':'Asignatura',
            'specialization':'Especialidad',
            'semester':'Semestre',
            'image':'Imagen'
        }
        widgets = {
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'specialization':forms.Select(attrs={'class':'form-control'}),
            'semester':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = [
            'idNote',
            'topic',
            'subject',
            'specialization',
            'written_in',
            'image'
        ]
        labels = {
            'idNote':'Apunte',
            'topic':'Tema',
            'subject':'Asignatura',
            'specialization':'Especialidad',
            'written_in':'Fecha de Creación',
            'image':'Imagen'
        }
        widgets = {
            'idNote':forms.TextInput(attrs={'class':'form-control'}),
            'topic':forms.TextInput(attrs={'class':'form-control'}),
            'subject':forms.Select(attrs={'class':'form-control'}),
            'specialization':forms.Select(attrs={'class':'form-control'}),
            'written_in':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }