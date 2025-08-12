from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Curso(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.CharField(max_length= 150)
    descripcion = models.TextField()
    precio = models.FloatField()   
    cupo = models.IntegerField( default= 20)
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]

    def __str__(self):
        return self.nombre
    
class Actividad(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Nombre del Curso")
    descripcion =RichTextField(verbose_name = "Comentario")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Creacion")
    
    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]
        
    def __str__(self):
        return self.descripcion
    
    
    