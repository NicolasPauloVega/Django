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
import miApp.views

urlpatterns = [
    path('holaMundo/', miApp.views.holaMundo, name="holaMundo"),
    path('saludo/<int:redirigir>', miApp.views.saludo, name="saludo"),
    path('', miApp.views.index, name="index"),
    path('presentacion/', miApp.views.presentacion, name="presentacion"),
    path('contacto/', miApp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>', miApp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellido>', miApp.views.contacto, name="contacto"),
    path('quienesSomos/', miApp.views.quienesSomos, name="QuienesSomos"),
    path('productosServicios/', miApp.views.productosServicios, name="ProductosServicios"),
    path('ejercicioBucle/', miApp.views.ejercicioBucle, name="ejercicioBucle"),
    path('pagina/', miApp.views.pagina, name="Página"),
    path('crear_articulo/', miApp.views.crear_articulo, name="Crear_articulo"),
    path('crear_articulo/<str:title>/<str:content>/<str:public>', miApp.views.crear_articulo, name="crear_articulo"),
    path('articulo/', miApp.views.articulo, name="Articulo"),
    path('editar_articulo/<int:id>', miApp.views.editar_articulo, name="Editar_Articulo"),
    path('articulos/', miApp.views.articulos, name="Listar"),
    path('borrar_articulo/<int:id>', miApp.views.borrar_articulo, name="Borrar"),
    path('delete_articulos/<int:id>', miApp.views.delete_articulos, name="delete_articulos"),
    path('update_articulo/<str:title>/<int:id>', miApp.views.update_articulo, name="Actualiazar SQL"),
    path('create_articulo/', miApp.views.create_articulo, name="Create"),
    path('save_articulo/', miApp.views.save_articulo, name="Save"),
    path('create-full-article/', miApp.views.create_full_articulo, name="create_full"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
