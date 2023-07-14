from django.shortcuts import render, redirect, reverse  

from .models import *
from .forms import *

def especialidades_crud(request):
    context = {'especialidades':Specialization.objects.all()}
    return render(request,'crud/especialidades.html',context)

def asignaturas_crud(request):
    context = {'asignaturas':Subject.objects.all()}
    return render(request,'crud/asignaturas.html',context)

def apuntes_crud(request):
    context = {'apuntes':Note.objects.all()}
    return render(request,'crud/apuntes.html',context)

def subjects_by_specialization_crud(request, specialization):
    try:
        subjects = Subject.objects.filter(specialization=specialization)
        if subjects:
            context = {'asignaturas': subjects }
            return render(request,'crud/asignaturas.html',context)
        else:
            return redirect(reverse('asignaturas-crud') + '?FAIL')
    except:
        return redirect(reverse('asignaturas-crud') + '?FAIL')


def specialization_new(request):
    if request.method == 'POST':
        form = SpecializationForm(request.POST, request.FILES)
        if form.is_valid():
            specialization = form.cleaned_data.get('specialization')
            image = form.cleaned_data.get('image')
            obj = Specialization.objects.create(
                specialization = specialization,
                image = image
            )
            obj.save()
            return redirect(reverse('especialidades-crud') + '?OK')
        else:
            return redirect(reverse('especialidades-crud') + '?FAIL')
    else:    
        form = SpecializationForm
    return render(request,'crud/specialization_new.html',{'form':form})

def specialization_detail(request,id):
    try:
        specialization = Specialization.objects.get(id=id)
        if specialization:
            context = {'especialidad':specialization}
            return render(request,'crud/specialization_detail.html',context)
        else:
            return redirect(reverse('especialidades-crud') + '?NO_EXIST')
    except:
        return redirect(reverse('especialidades-crud') + '?NO_EXIST')


def specialization_edit(request,id):
    try:
        specialization = Specialization.objects.get(id=id)
        form = SpecializationForm(instance = specialization)

        if request.method == 'POST':
            form = SpecializationForm(request.POST, request.FILES, instance = specialization)
            if form.is_valid():
                form.save()
                return redirect(reverse('especialidades-crud') + '?UPDATED')
            else:
                return redirect(reverse('specialization-edit') + id)

        context = {'form':form}
        return render(request,'crud/specialization_edit.html',context)
    except:
        return redirect(reverse('especialidades-crud') + '?NO_EXIST')

def specialization_delete(request,id):
    try:
        specialization = Specialization.objects.get(id=id)
        specialization.delete()
        return redirect(reverse('especialidades-crud') + '?DELETED')
    except:
        return redirect(reverse('especialidades-crud') + '?FAIL')


def subject_new(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            specialization = form.cleaned_data.get('specialization')
            semester = form.cleaned_data.get('semester')
            image = form.cleaned_data.get('image')
            obj = Subject.objects.create(
                subject = subject,
                specialization = specialization,
                semester = semester,
                image = image
            )
            obj.save()
            return redirect(reverse('asignaturas-crud') + '?OK')
        else:
            return redirect(reverse('asignaturas-crud') + '?FAIL')
    else:    
        form = SubjectForm
    return render(request,'crud/subject_new.html',{'form':form})

def subject_detail(request,id):
    try:
        subject = Subject.objects.get(id=id)
        if subject:
            context = {'asignatura':subject}
            return render(request,'crud/subject_detail.html',context)
        else:
            return redirect(reverse('asignaturas-crud') + '?NO_EXIST')
    except:
        return redirect(reverse('asignaturas-crud') + '?NO_EXIST')


def subject_edit(request,id):
    try:
        subject = Subject.objects.get(id=id)
        form = SubjectForm(instance = subject)

        if request.method == 'POST':
            form = SubjectForm(request.POST, request.FILES, instance = subject)
            if form.is_valid():
                form.save()
                return redirect(reverse('asignaturas-crud') + '?UPDATED')
            else:
                return redirect(reverse('asignaturas-edit') + id)

        context = {'form':form}
        return render(request,'crud/subject_edit.html',context)
    except:
        return redirect(reverse('asignaturas-crud') + '?NO_EXIST')

def subject_delete(request,id):
    try:
        subject = Subject.objects.get(id=id)
        subject.delete()
        return redirect(reverse('asignaturas-crud') + '?DELETED')
    except:
        return redirect(reverse('asignaturas-crud') + '?FAIL')



def note_new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            idNote = form.cleaned_data.get('idNote')
            topic = form.cleaned_data.get('topic')
            subject = form.cleaned_data.get('subject')
            specialization = form.cleaned_data.get('specialization')
            written_in = form.cleaned_data.get('written_in')
            image = form.cleaned_data.get('image')
            obj = Note.objects.create(
                idNote = idNote,
                topic = topic,
                subject = subject,
                specialization = specialization,
                written_in = written_in,
                image = image
            )
            obj.save()
            return redirect(reverse('apuntes-crud') + '?OK')
        else:
            return redirect(reverse('apuntes-crud') + '?FAIL')
    else:    
        form = NoteForm
    return render(request,'crud/note_new.html',{'form':form})


def note_detail(request,idNote):
    try:
        note = Note.objects.get(idNote=idNote)
        if note:
            context = {'apunte':note}
            return render(request,'crud/note_detail.html',context)
        else:
            return redirect(reverse('apuntes-crud') + '?NO_EXIST')
    except:
        return redirect(reverse('apuntes-crud') + '?NO_EXIST')


def note_edit(request,idNote):
    try:
        note = Note.objects.get(idNote=idNote)
        form = NoteForm(instance = note)

        if request.method == 'POST':
            form = NoteForm(request.POST, request.FILES, instance = note)
            if form.is_valid():
                form.save()
                return redirect(reverse('apuntes-crud') + '?UPDATED')
            else:
                return redirect(reverse('apuntes-edit') + idNote)

        context = {'form':form}
        return render(request,'crud/note_edit.html',context)
    except:
        return redirect(reverse('apuntes-crud') + '?NO_EXIST')

def note_delete(request,idNote):
    try:
        note = Note.objects.get(idNote=idNote)
        note.delete()
        return redirect(reverse('apuntes-crud') + '?DELETED')
    except:
        return redirect(reverse('apuntes-crud') + '?FAIL')

