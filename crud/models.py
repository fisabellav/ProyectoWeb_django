from django.db import models

class Specialization(models.Model):
    specialization = models.CharField(verbose_name='Especialidad', max_length=50)
    image = models.ImageField(verbose_name='Imagen',upload_to='especialidades',null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'especialidad'
        verbose_name_plural = 'especialidades'
        ordering = ['specialization']

    def __str__(self) -> str:
        return self.specialization

class Subject(models.Model):
    subject = models.CharField(verbose_name='Asignatura', max_length=50)
    specialization = models.ForeignKey(Specialization,verbose_name='Especialidad',on_delete=models.CASCADE)
    semester = models.IntegerField(verbose_name='Semestre')
    image = models.ImageField(verbose_name='Imagen',upload_to='asignaturas',null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'asignatura'
        verbose_name_plural = 'asignaturas'
        ordering = ['subject']

    def __str__(self) -> str:
        return self.subject


class Note(models.Model):
    idNote = models.CharField(primary_key=True,verbose_name='ID',max_length=20)
    topic  = models.CharField(verbose_name='Tema', max_length=50)
    subject = models.ForeignKey(Subject,verbose_name='Asignatura',on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization,verbose_name='Especialidad',on_delete=models.CASCADE)
    written_in = models.DateField(verbose_name='Fecha de creación')
    image = models.ImageField(verbose_name='Imagen',upload_to='asignaturas',null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'apunte'
        verbose_name_plural = 'apuntes'
        ordering = ['idNote']

    def __str__(self) -> str:
        return self.topic