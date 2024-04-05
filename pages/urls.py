from django.urls import path

#Importamos las vistas en la url
from .views import *

urlpatterns = [
    path('pagina/', page, name="page"),
    path('pagina/<str:slug>', page, name="page"),
]
