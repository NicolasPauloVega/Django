from django.shortcuts import render
from .models import Tarea
# Create your views here.

def home(request):
    tarea = Tarea.objects.all()
    context = {'tareas': tarea}
    return render(request, 'home.html',context)