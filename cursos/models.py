from django.db import models

# Create your models here.
class Curso(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.CharField(max_length= 50)
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
    