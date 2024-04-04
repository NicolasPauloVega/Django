from django.shortcuts import render, HttpResponse, redirect
from my_app.models import Article, Category

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

#vistas para el apartado de hola mundo
def hello_world(request):
    return render(request, 'page/hello_world.html')

#vistas para el apartado del inicio
def index(request):
    # template = """
    #                 <h1>Inicio</h1>
    #                 <p>Años hasta el 2050</p>
    #                 <ul>
    #             """

    # while year <= 2050:
    #     template += f"<li> {str(year)} </li>"
    #     year += 1
    # template += "</ul>"
    
    year = 2024
    hasta = range(year, 2050)

    nombre = 'Nicolas Paulo Vega'
    lenguajes = ['JavaScripts', 'Python', 'PHP', 'C']

    return render(request, 'page/index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta,
    })

#vistas para el apartado de informacion de pagina
def page(request, redirects=0):
    if redirects==1:
        return redirect('contact', name="Ana", last_name="Perez")
    return render(request, 'page/page.html', {
        'text':'Este es mi texto',
        'list': ['uno', 'dos', 'tres'],
    })

#vistas para el apartado de bienvenida
def welcome(request):
    return render(request, 'page/welcome.html')

#vistas para el apartado de contacto
def contact(request, name="", last_name=""):
    html = ""
    if name and last_name:
        html = "<h2>Nombre Completo: </h2>"
        html += f"<h3> {name} {last_name} </h3>"
    return HttpResponse(f"<h2>Contacto </h2>"+html)

#vistas para articulos
def article(request):
    # try:
    #     article = Article.objects.get(pk=1)
    #     reponse = f"Articulo: <br/> {article.id} {article.title}"
    # except:
    #     reponse = "<h1> Articulo no encontrado </h1>"
    # return HttpResponse(reponse)
    article = Article.objects.all()
    return render(request, 'article/article.html', {'articles': article})

def create_article(request,title,content,public):#Crear articulos
    article = Article(
        title = title,
        content = content,
        public = public,
    )
    article.save()
    return HttpResponse(f"Articulo creado: {article.title} - {article.content} ")

def update_article(requets, id):#Editar articulos
    article = Article.objects.get(pk=id)
    article.title="SENA 2024"
    article.content="Servicio Nacional de Aprendizaje"
    article.public=True

    article.save()
    return HttpResponse(f"Articulo Editado: {article.title} - {article.content}")