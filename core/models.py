from django.db import models

class User(models.Model):
    rut = models.CharField(primary_key=True,verbose_name='RUT',max_length=20)
    name  = models.CharField(verbose_name='NOMBRE', max_length=50)
    last_name =  models.CharField(verbose_name='APELLIDO', max_length=50)
    birthday = models.DateField(verbose_name='FECHA DE NACIMIENTO')
    mail = models.CharField(verbose_name='CORREO', max_length=50)

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        ordering = ['last_name']

    def __str__(self) -> str:
        return self.rut
