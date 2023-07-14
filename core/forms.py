from django import forms
from django.forms import ModelForm
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'rut',
            'name',
            'last_name',
            'birthday',
            'mail'
        ]
        labels = {
            'rut':'Rut',
            'name':'Nombre',
            'last_name':'Apellido',
            'birthday':'Fecha de nacimiento',
            'mail':'Correo'
        }
        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ej. 12345678-9', 'id':'txtRut'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su nombre', 'id':'nombre'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su apellido', 'id':'apellido'}),
            'birthday':forms.DateInput(attrs={'class':'form-control', 'type':'date', 'id':'fecha_nac'}),
            'mail':forms.TextInput(attrs={'class':'form-control', 'type':'email', 'placeholder':'correo@correo.com', 'id':'email'})
        }