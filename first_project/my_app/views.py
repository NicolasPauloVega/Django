from django.shortcuts import render, HttpResponse, redirect
from django.db import connection  
from miApp.models import Article
from miApp.forms import FormArticulo
from django.contrib import messages


# Create your views here.
def holaMundo(request):
    return render(request, 'holaMundo.html')

def saludo(request, redirigir=0):
    if redirigir == 1:
        return redirect('contacto', nombre='ana', apellido='a')
    return render(request, 'saludo.html')

from django.shortcuts import render, HttpResponse, redirect
from miApp.models import Article

 
def index(request):
    years = list(range(2024, 2051))
    leap_years = [year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
    even_years = [year for year in years if year % 2 == 0]
    odd_years = [year for year in years if year % 2 != 0]

    return render(request, 'index.html', {
        'mi_variable': 'soy un dato que está en la vista',
        'title': 'Inicio de Sitio',
        'titulo': 'Página de Inicio Sena',
        'name': 'nombre',
        'years': years,
        'leap_years': leap_years,
        'even_years': even_years,
        'odd_years': odd_years,
    })

def presentacion(request):
    # return HttpResponse(layout+"""
    #                     <h2> Nombre: Kevin Hernandez <br> Numero: 3224634734 <br> Email: kevinhp2006@gmail.com </h2>
    #                     """)
    return render(request, 'presentacion.html')

def contacto(request, nombre="", apellido=""):
    aprendiz = ""
    if nombre and apellido:
        aprendiz = "<h2> Nombre Completo: </h2>"
        aprendiz += f"<h3> {nombre} {apellido}</h3>"
    elif nombre:
        aprendiz = "<h2> Nombre: </h2>"
        aprendiz += f"<h3> {nombre} </h3>"
    return render(request, 'contacto.html')

def quienesSomos(request):
    return render(request, 'quienesSomos.html')

def productosServicios(request):
    return render(request, 'productosServicios.html')


def ejercicioBucle(request):
    # Imprimir los números del 1 al 10 utilizando un bucle while
    numerosWhile = []
    numero = 1
    while numero <= 10:
        numerosWhile.append(numero)
        numero += 1

    # Calcular la suma de los números del 1 al 10 utilizando un bucle for
    suma = 0
    for num in range(1, 11):
        suma += num

    return render(request, 'ejercicioBucle.html', {
        'numerosWhile': numerosWhile,
        'suma': suma
    })
    
def pagina(request,redirigir = 0):
    if redirigir == 1:
        return redirect('contacto', nombre ="Sofia", apellidos = "Perez")
    return render(request,'pagina.html' , {'texto':'Este es mi texto', 'lista':['uno','dos','tres'],})

def crear_articulo(request,title,content,public):
    articulo = Article(
        title = title,
        content = content,
        public = public,
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} ")
    
def articulo (request):
   try:
       articulo = Article.objects.get(pk=3, public=True)
       response = f"Articulo Consultado {articulo.title} - {articulo.content} - Estado: {articulo.public}"
       
   except:
       response = "<strong>Articulo no encontrado</strong>" 
       
       return HttpResponse(response)
   
def editar_articulo(request,id):
    articulo = Article.objects.get(pk=id)
    articulo.title="Los 12 Cuentos peregrinos"
    articulo.public=True
    articulo.save()
    return HttpResponse(f"El articulo {articulo.id} de nombre: {articulo.title} ha sido actualizado y su estado es {articulo.public}")

def articulos (request):
    articulos = Article.objects.all()
    return render(request, 'articulos.html',{
        'articulos':articulos
    })

# def articulos(request):
    # La última asignación sobrescribe las anteriores, por lo que solo esta tiene efecto.
    # articulos = Article.objects.order_by('id')
    # articulos = Article.objects.filter(title = "articulo 4")
    # articulos = Article.objects.filter(public = "True",id=4)
    # articulos = Article.objects.filter(title__contains="articulos")
    # articulos = Article.objects.filter(title__exact="articulos")
    # articulos = Article.objects.filter(title__iexact="rticulos")
    # articulos = Article.objects.filter(title__iexact="articulos 4")
    # articulos = Article.objects.filter(id__gt=1)
    # articulos = Article.objects.filter(id__lte=5)
    # articulos = Article.objects.filter(id__in=[1,2,9,10])
    
    # Aquí deberías seleccionar una sola consulta a la vez.
    # articulos = Article.objects.filter(
    #     title__contains="Art",
    # ).exclude(
    #     public=True
    # )
    
    # # O bien puedes utilizar una consulta cruda.
    # # articulos = Article.objects.raw("SELECT * FROM miApp_article WHERE content like 'L%' AND public = 1")
    
    # return render(request, 'articulos.html', {
    #     'articulos': articulos
    # })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('Listar')

def delete_articulos(request, id):
   sql_query = "DELETE FROM miApp_article WHERE id = %s"
   with connection.cursor() as cursor:
       cursor.execute(sql_query, [id])
       return redirect('Listar')


def update_articulo(request, title, id):
    sql_query = "UPDATE miApp_article SET title = %s WHERE id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql_query, [title, id])
        articulos = Article.objects.all()
    return render(request, 'articulos.html', {'articulos': articulos})

def save_articulo(request):
    if request.method == 'POST':
        title = request.POST["title"]
        if len(title)<=4:
            return HttpResponse(f"El titulo del Articulo debe ser mayor a 5 caracteres")
        else:
            content = request.POST['content']
            public = request.POST['public']
                
        articulo = Article(
            title = title,
            content = content,
            public = public,
        )
        articulo.save()
        return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")
    else:
        return HttpResponse(f"El Artículo no fue creado")

def create_articulo(request):
    return render (request, 'create_articulo.html')

def create_full_articulo(request):
    if request.method == 'POST':
        formulario = FormArticulo(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title = data_form.get('title')
            content = data_form.get('content')
            public = data_form.get('public')
            
            articulo = Article(
                title = title,
                content = content,
                public = public,
             )
            articulos = Article.objects.all().order_by('content')
            articulo.save()
            
            messages.success(request, f'El articulo {articulo.id} se ha guardado satisfactoriamente')
            # return HttpResponse (title + ' ' + content + ' ' + str(public) )
            
            return render(request,'articulos.html',{
                'titulo':'Guardado el articulo con Éxito',
                'icono': 'success',
                'boton' : 'Aceptar',
                'articulos': articulos
            })
        else:
            
            return render(request, 'create_full_articulo.html',{
                'form':formulario})
        
    else:
       formulario = FormArticulo()
       return render(request, 'create_full_articulo.html',{
           'form':formulario
        })