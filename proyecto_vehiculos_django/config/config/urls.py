"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vehiculo.views import pruebaView, indexView, catalogoView, registroView, loginView, logoutView, listaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name = 'index'),
    path('prueba/', pruebaView, name = 'prueba'),
    path('vehiculo/add', catalogoView, name = 'catalogo'),
    path('registro/', registroView, name='registro'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('listar/', listaView, name='listar'),
]
