from django.shortcuts import get_object_or_404, redirect, render
from .models import Curso
from .forms import CursoForm

# Create your views here.

#Accedemos al modelo Comentarios que contiene la estructura de la tabla.
def cursos(request):
    cursos=Curso.objects.all()
#all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"cursos/cursos.html",{'cursos':cursos})
#Indicamos el lugar donde se renderizará el resultado de esta vista y enviamos la lista de alumnos recuparados

def registrar(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return redirect('Cursos')
    form = CursoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'cursos/AgregarCurso.html',{'form': form})


def eliminarCurso(request, id, confirmacion='cursos/confirmarEliminacion.html'):
    curso = get_object_or_404(Curso, id=id)
    if request.method=='POST':
        curso.delete()
        cursos=Curso.objects.all()
        return render(request,"cursos/cursos.html",{'cursos':cursos})

    return render(request, confirmacion, {'object':curso})

def consultarCursoIndividual(request, id):
    curso=Curso.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objetos
    #del modelo que cumple la condición (registro de la tabla ComentariosContacto.
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su
    #consulta.
    return render(request,"cursos/formEditarCurso.html",{'curso':curso})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados.
    
def editarCurso(request, id):
    curso = get_object_or_404(Curso, id=id)
    form = CursoForm(request.POST, request.FILES, instance=curso)
    #Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        cursos=Curso.objects.all()
        return render(request,"cursos/cursos.html",{'cursos':cursos})
    #Si el formulario no es valido nos regresa al formulario para verificar
    #datos
    return render(request,"cursos/formEditarCurso.html",{'curso':curso})