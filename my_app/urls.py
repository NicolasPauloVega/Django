from django.urls import path

#Importamos las vistas en la url
from .views import *

urlpatterns = [
    #links para el inicio
    path('', index, name="start"),
    path('index/', index, name="index"),
    
    #links para la parte de la bienvenida
    path('welcome/', welcome, name="welcome"),

    #links para hola mundo
    path('hello-world/', hello_world, name="hello_world"),

    #links para la pgina del sitio web
    path('test-page/', page, name="pages"),
    path('test-page/<int:redirects>', page, name="pages"),

    #links para el contacto
    path('contact/', contact, name="contact"),
    path('contact/<str:name>', contact, name="contact"),
    path('contact/<str:name>/<str:last_name>', contact, name="contact"),

    #links para el articulo
    path('article/', article, name="article"),
    path('create-article/', create_article, name="create_article"),
    path('create-article/<str:title>/<str:content>/<str:public>', create_article, name="create_article"),
    path('update-article/<int:id>', update_article, name="update_article"),
]
