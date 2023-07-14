from django.shortcuts import render, HttpResponse, redirect, reverse
from crud.models import *
from .models import *
from .forms import *
# Create your views here.


def index(request):
    return render(request,'core/index.html')

def especialidades(request):
    context = {'especialidades':Specialization.objects.all()}
    return render(request,'core/especialidades.html',context)

def asignaturas(request):
    context = {'asignaturas':Subject.objects.all()}
    return render(request,'core/asignaturas.html',context)

def subjects_by_specialization(request, specialization):
    try:
        subjects = Subject.objects.filter(specialization=specialization)
        if subjects:
            context = {'asignaturas': subjects }
            return render(request,'core/asignaturas.html',context)
        else:
            return redirect(reverse('especialidades') + '?FAIL')
    except:
        return redirect(reverse('especialidades') + '?FAIL')

def notes_by_subject(request, subject):
    try:
        notes = Note.objects.filter(subject=subject)
        if notes:
            context = {'apuntes': notes }
            return render(request,'core/apuntes.html',context)
        else:
            return redirect(reverse('asignaturas') + '?FAIL')
    except:
        return redirect(reverse('asignaturas') + '?FAIL')

def apuntes(request):
    context = {'apuntes':Note.objects.all()}
    return render(request,'core/apuntes.html',context)

def contacto(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            rut = form.cleaned_data.get('rut')
            name = form.cleaned_data.get('name')
            last_name = form.cleaned_data.get('last_name')
            birthday = form.cleaned_data.get('birthday')
            mail = form.cleaned_data.get('mail')
            obj = User.objects.create(
                rut = rut,
                name = name,
                last_name = last_name,
                birthday = birthday,
                mail = mail
            )
            obj.save()
            return redirect(reverse('contacto') + '?OK')
        else:
            return redirect(reverse('contacto') + '?FAIL')
    else:    
        form = UserForm
    return render(request,'core/contacto.html',{'form':form})

def nosotros(request):
    return render(request,'core/nosotros.html')

def recursos(request):
    return render(request,'core/recursos.html')
