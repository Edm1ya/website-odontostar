from django.db import models

# Create your models here.
class Contact(models.Model):
    title = models.CharField(max_length=100, verbose_name='Nombre')
    mail = models.EmailField(verbose_name='Correo Electronico')
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')

    class Meta:
        verbose_name='Contacto'
        verbose_name_plural='Contactos'
        ordering = ['-created']

    def __str__(self):
        return self.name