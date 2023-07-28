from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VehiculoForm, RegistroUserForm
from django.http import HttpResponse, HttpResponseRedirect
from tokenize import PseudoExtras
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import VehiculoModel



# Create your views here.
def pruebaView(request):
    context = {}
    return render(request, 'test.html', context)
    

def indexView(request):
    context = {}
    return render(request, 'index.html', context)

def catalogoView(request):
    form = VehiculoForm(request.POST or None, request.FILES or None)
    permiso_agregar_catalogo = request.user.has_perm('vehiculo.can_add_vehiculo_model')
    context = {'form' : form, 'permiso_agregar_catalogo': permiso_agregar_catalogo}
    if form.is_valid():
        form.save()
        form = VehiculoForm()
        messages.success(request, 'los datos se han guardado exitosamente.')
    return render(request, 'catalogo.html', context)

def listaView(request):
    vehiculos = VehiculoModel.objects.all()
    permiso_visualizar_catalogo = request.user.has_perm('vehiculo.visualizar_catalogo')
    context = {'listaVehiculos': vehiculos, 'permiso_visualizar_catalogo': permiso_visualizar_catalogo}
    return render(request, 'lista.html', context)

def registroView(request):
    if request.method == "POST":
        form = RegistroUserForm(request.POST)   
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(VehiculoModel)
            visualizar_catalogo = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)

            user = form.save()

            user.user_permissions.add(visualizar_catalogo)

            login(request, user)
            messages.success(request, 'Usuario registrado de forma exitosa en nuestra web')
            return HttpResponseRedirect('/')  
        messages.error(request, "Registro inválido, por favor verifique los datos ingresados.")

    form = RegistroUserForm()
    context = {'register_form': form}
    return render(request, 'registro.html', context)

def loginView(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Has iniciado sesion como {username}")
                return HttpResponseRedirect("/")
            else:
                messages.error(request, "usuario o contraseña incorrectos")
        else:
            messages.error(request, "usuario o contraseña incorrectos")
    form = AuthenticationForm()
    context = {"login_form":form}
    return render(request, "login.html", context)


def logoutView(request):
    logout(request)
    return HttpResponseRedirect("/login")

