from django.db import models

class Tarea(models.Model):
    tareas=models.CharField(max_length=100)
    def __str__(self):
        return self.tareas

# Create your models here.
