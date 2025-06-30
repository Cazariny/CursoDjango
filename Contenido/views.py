from django.shortcuts import render, HttpResponse

def principal(request):
    return render(request, 'Contenido/principal.html')

def contacto(request):
    return render(request, 'Contenido/contacto.html')
    
def cursos(request): 
    return render(request, 'Contenido/cursos.html')