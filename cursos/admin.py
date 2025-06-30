from django.contrib import admin
from .models import Curso

# Register your models here.



class AdminModel(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'cupo')
    search_fields = ('id', 'nombre')
    date_hierarchy = 'created'
    list_filter = ('nombre',)
    
admin.site.register(Curso ,AdminModel)