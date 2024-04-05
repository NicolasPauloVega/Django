from django.shortcuts import render, HttpResponse, redirect
from my_app.models import Article, Category
from django.db.models import Q
from my_app.forms import FormArticle
from django.contrib import messages

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

    """
        consulta de articulos:

        article = Article.object.order_by('title') --> Filtramos un por titulo.

        article = Article.object.order_by('-title') --> Filtramos por un titulo pero de atras para adelante.

        article = Article.object.order_by('title')[:3] --> Filtramos por un titulo pero mostramos los primeros 3.

        article = Article.object.order_by('title')[3:7] --> Filtramos por un titulo pero mostramos del 3 al 7.

        article = Article.object.filter(title="SENA 2024") --> Filtramos por un titulo que contenga "SENA 2024"

        article = Article.object.filter(title__contains="rticulo") --> Filtramos por un título que contenga "rticulo".

        article = Article.object.filter(title__exact="rticulo") --> Filtramos por un título exacto "rticulo".

        article = Article.object.filter(title__iexact="rticulo") --> Filtramos por un título exacto "rticulo" de manera insensible a mayúsculas y minúsculas.

        article = Article.object.filter(id__gt=9) --> Filtramo por un ID que sea mayor que 9.

        article = Article.object.filter(id__gte=9) --> Filtramos por un ID que sea mayor o igual a 9.

        article = Article.object.filter(id__lt=9) --> Filtramos por un ID que sea menor que 9.

        article = Article.object.filter(id__lt=9, title__contains="article") --> Filtramos por un ID que sea menor que 9 y un título que contenga "article".

        # article = Article.object.filter(
        #                                 title__contrains="Arti",
        #                                 public=True
        #                             )

        # article = Article.object.filter(
        #                                 title_contrains="Arti",
        #                             ).execute(
        #                                 public=True
        #                             )

        article = Article.object.raw("select * from my_app_article where title like 'Article %' and public=0") --> Se ejecuta una consulta SQL para poder mostrar todos los registros de la tabla article.

        article = Article.object.filter(Q(title__contrains="2") | Q(title__contrains="4")) --> utilizamos el metodo or para poder realizar una consulta cuyos titulos sean "2" y "4". 
    """
    
    article = Article.objects.all()
    return render(request, 'article/article.html', {'articles': article})

def save_article(request):#guardar articulos
    if request.method=='POST':
        title= request.POST['title']
        if len(title)<=5:
            return HttpResponse("<h2>El titulo debe ser mayor a 5 caracteres</h2>")
        content= request.POST['content']
        public= request.POST['public']
        article = Article(
            title = title,
            content = content,
            public = public,
        )
        article.save()
        return HttpResponse(f"Articulo creado: {article.title} - {article.content} ")
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")


def create_article(request):#Crear articulos
    return render(request, 'article/create_article.html')

def create_full_article(request):
    if request.method=='POST':
        form= FormArticle(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            title = data_form.get('title')
            content = data_form.get('content')
            public = data_form.get('public')

            article= Article(
                title=title,
                content=content,
                public=public,
            )
            article.save()
            messages.success(request, f'El articulo {article.id} se ha guardado satisfactoriamente')
            # return HttpResponse(article.title+' - '+article.content+'- '+str(article.public))
            return redirect('article')
        else:
            return render(request, 'article/create_full_article.html', {
                'form': form
            })
    else:
        form = FormArticle()
        return render(request, 'article/create_full_article.html', {
            'form': form
        })

def update_article(requets, id):#Editar articulos
    article = Article.objects.get(pk=id)
    article.title="SENA 2024"
    article.content="Servicio Nacional de Aprendizaje"
    article.public=True

    article.save()
    return HttpResponse(f"Articulo Editado: {article.title} - {article.content}")

def delete_article(request, id):#Eliminar articulos
    article = Article.objects.get(pk=id)
    article.delete()
    return redirect('article')