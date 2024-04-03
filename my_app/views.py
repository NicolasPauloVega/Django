from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# layout ="""
#             <h1>Sitio Web con Django | Nicolas Paulo Vega</h1>
#             <hr>
#             <ul>
#                 <li>
#                     <a href="/welcome">Bienvenido</a>
#                 </li>
#                 <li>
#                     <a href="/index">Inicio</a>
#                 </li>
#                 <li>
#                     <a href="/hello-world">Hola mundo</a>
#                 </li>
#                 <li>
#                     <a href="/test-page">Página</a>
#                 </li>
#             </ul>
#         """

def hello_world(request):
    return render(request, 'hello_world.html')

def index(request):
    year = 2024
    while year <= 2050:
        f"<li> {str(year)} </li>"
        year += 1
    return render(request, 'index.html')

def page(request, redirects=0):
    if redirects==1:
        return redirect('contact', name="Ana", last_name="Perez")
    return render(request, 'page.html')

def welcome(request):
    return render(request, 'welcome.html')

def contact(request, name="", last_name=""):
    html = ""
    if name and last_name:
        html = "<h2>Nombre Completo: </h2>"
        html += f"<h3> {name} {last_name} </h3>"
    return HttpResponse(f"<h2>Contacto </h2>"+html)

