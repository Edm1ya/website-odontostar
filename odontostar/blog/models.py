from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualizacion")
    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    content =  RichTextField(verbose_name="Contenido")
    img = models.ImageField(upload_to='media/blog/', verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualizacion")
    categories = models.ManyToManyField(Category, verbose_name="Categorias" )
    author = models.ForeignKey(User, verbose_name="autor", on_delete=models.CASCADE)

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
        ordering = ['created']

    def __str__(self):
        return self.title
