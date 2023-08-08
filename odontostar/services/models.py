from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = RichTextField(verbose_name="Descripcion")
    image = models.ImageField(upload_to='media/services/', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')

    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'
        ordering = ['-created']

    def __str__(self):
        return self.name