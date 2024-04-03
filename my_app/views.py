from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layout ="""
            <h1>Sitio Web con Django | Nicolas Paulo Vega</h1>
            <hr>
            <ul>
                <li>
                    <a href="/welcome">Bienvenido</a>
                </li>
                <li>
                    <a href="/index">Inicio</a>
                </li>
                <li>
                    <a href="/hello-world">Hola mundo</a>
                </li>
                <li>
                    <a href="/test-page">Página</a>
                </li>
            </ul>
        """

def hello_world(request):
    return HttpResponse(
        """
            <h1>Hola mundo</h1>
            <h3>Sena todos ustedes bienvenidos!!</h3>
        """
    )

def index(request):
    template = """
                    <h1>Inicio</h1>
                    <p>Años hasta el 2050</p>
                    <ul>
                """
    year = 2024
    while year <= 2050:
        template += f"<li> {str(year)} </li>"
        year += 1
    return HttpResponse(layout+template)

def page(request, redirects=0):
    if redirects==1:
        return redirect('contact', name="Ana", last_name="Perez")
    return HttpResponse(
        """
            <h1>Pagina de mi web</h1>
            <p>Creado por Nicolas Paulo Vega</p>
        """
    )

def welcome(request):
    return HttpResponse('Hola Mundo desde Django')

def contact(request, name="", last_name=""):
    html = ""
    if name and last_name:
        html = "<h2>Nombre Completo: </h2>"
        html += f"<h3> {name} {last_name} </h3>"
    return HttpResponse(layout+f"<h2>Contacto </h2>"+html)

