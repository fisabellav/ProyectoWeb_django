from django.contrib import admin
from .models import Specialization, Subject, Note

# Register your models here.
class SpecializationAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('id','specialization')
    ordering = ('specialization',)

class SubjectAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','subject')
    ordering = ('subject',)

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('idNote',)
    ordering = ('idNote',)

admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Note,NoteAdmin)
