from django.shortcuts import render,redirect
from django.views import View

# Create your views here.

from mi_aplicacion.models import Escuela,Maestro,Alumno
from mi_aplicacion.forms import EscuelaForm

class Home(View):
    def get(self,request):
        cdx={
            "titulo":"Home",
            "subtitulo":"Bienvenido a mi aplicacion"

        }
        return render(request, "home/home.html",cdx)

class Escuelas(View):
    def get(self, request):
        escuelas = Escuela.objects.all()
        cdx = {
            "titulo":"Escuelas",
            "subtitulo":"Listado de escuelas",
            "escuelas": escuelas
        }
        return render(request, "Escuelas/escuelas.html",cdx)
    
class EscuelaAlta(View):

    def get(self, request):
        form = EscuelaForm()
        return render(request, 'escuelas/alta.html', {
            "subtitulo": "Escuela alta",
            "titulo": "Escuela Alta",
            "form": form
        })
    
    def post(self, request):
        form = EscuelaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('escuelas')  

        return render(request, 'escuelas/alta.html', {
            "titulo": "Escuela",
            "form": form,
            "mensaje": "Error al crear la escuela"
        })
        
class EscuelaEditar(View):
    def get(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx = {
            "titulo":"Escuela",
            "form":form,
            "subtitulo":"Escuela Cambios"
        }
        return render(request, 'escuelas/editar.html',cdx)
    
    def post(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST, request.FILES, instance = escuela)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        return redirect('home')

class EscuelaEliminar(View):
    def get(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx = {
            "titulo":"Escuela",
            "form":form,
            "subtitulo":"Escuela Eliminar"
        }
        return render(request, 'escuelas/editar.html',cdx)
    
    def post(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST, request.FILES, instance = escuela)
        if form.is_valid():
            escuela.delete()
            return redirect('escuelas')
        return redirect('home')    

class Maestros(View):
    def get(self, request):
        maestros = Maestro.objects.all()
        cdx = {
            "titulo":"Maestros",
            "subtitulo":"Listado de Maestros",
            "maestros": maestros
        }
        return render(request, "maestros/maestros.html",cdx)    