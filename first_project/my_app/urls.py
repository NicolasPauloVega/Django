"""
URL configuration for primerProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('holaMundo/', holaMundo, name="holaMundo"),
    path('saludo/<int:redirigir>', saludo, name="saludo"),
    path('', index, name="index"),
    path('presentacion/', presentacion, name="presentacion"),
    path('contacto/', contacto, name="contacto"),
    path('contacto/<str:nombre>', contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellido>', contacto, name="contacto"),
    path('quienesSomos/', quienesSomos, name="QuienesSomos"),
    path('productosServicios/', productosServicios, name="ProductosServicios"),
    path('ejercicioBucle/', ejercicioBucle, name="ejercicioBucle"),
    path('pagina/', pagina, name="Página"),
    path('crear_articulo/', crear_articulo, name="Crear_articulo"),
    path('crear_articulo/<str:title>/<str:content>/<str:public>', crear_articulo, name="crear_articulo"),
    path('articulo/', articulo, name="Articulo"),
    path('editar_articulo/<int:id>', editar_articulo, name="Editar_Articulo"),
    path('articulos/', articulos, name="Listar"),
    path('borrar_articulo/<int:id>', borrar_articulo, name="Borrar"),
    path('delete_articulos/<int:id>', delete_articulos, name="delete_articulos"),
    path('update_articulo/<str:title>/<int:id>', update_articulo, name="Actualiazar SQL"),
    path('create_articulo/', create_articulo, name="Create"),
    path('save_articulo/', save_articulo, name="Save"),
    path('create-full-article/', create_full_articulo, name="create_full"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
