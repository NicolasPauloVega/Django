from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateField(auto_now = True)

    @classmethod
    def get_next_code(cls):
        # Método para obtener el próximo código disponible sumando 1 al código del último registro
        # Ordenamos los registros por código de manera descendente y obtenemos el primer registro
        last_record = cls.objects.order_by('-code').first()
        if last_record:
            # Si hay registros, sumamos 1 al código del último registro
            return last_record.code + 1
        else:
            # Si no hay registros, el próximo código será 1
            return 1

    def save(self, *args, **kwargs):
        # Método para guardar el objeto Materi en la base de datos
        if not self.code:
            # Verificamos si el campo code ya tiene un valor asignado
            # Si no tiene un valor (es decir, es None o no está definido), asignamos el próximo código disponible
            self.code = self.get_next_code()
        # Llamamos al método save de la clase padre para guardar el objeto en la base de datos
        super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    create_date = models.DateField()

    @classmethod
    def get_next_code(cls):
        # Método para obtener el próximo código disponible sumando 1 al código del último registro
        # Ordenamos los registros por código de manera descendente y obtenemos el primer registro
        last_record = cls.objects.order_by('-code').first()
        if last_record:
            # Si hay registros, sumamos 1 al código del último registro
            return last_record.code + 1
        else:
            # Si no hay registros, el próximo código será 1
            return 1

    def save(self, *args, **kwargs):
        # Método para guardar el objeto Materi en la base de datos
        if not self.code:
            # Verificamos si el campo code ya tiene un valor asignado
            # Si no tiene un valor (es decir, es None o no está definido), asignamos el próximo código disponible
            self.code = self.get_next_code()
        # Llamamos al método save de la clase padre para guardar el objeto en la base de datos
        super().save(*args, **kwargs)