from django.shortcuts import render

# Create your views here.
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
    return render(request, 'index.html')
