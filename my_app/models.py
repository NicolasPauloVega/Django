from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="articles")
    public = models.BooleanField(verbose_name="¿Publicado?")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        #dab_table=""
        verbose_name="Articulo"
        verbose_name_plural="Articulos"
        ordering=['id']

    #Creamos un metodo magico.
    def __str__(self):
        if self.public:
            publico="(Publicado)"
        else:
            publico="(Privado)"
        return f"{self.title} -> {publico}"

    @classmethod
    def get_next_code(cls):
        last_record = cls.objects.order_by('-id').first()
        if last_record:
            return last_record.id + 1
        else:
            return 1

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.get_next_code()
        super().save(*args, **kwargs)

class Category(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    name = models.CharField(max_length=110, verbose_name="Nombre")
    description = models.CharField(max_length=250, verbose_name="Descripción")
    create_date = models.DateField(verbose_name="Fecha de creación")

    class Meta:
        #dab_table=""
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering=['-id']

    @classmethod
    def get_next_code(cls):
        last_record = cls.objects.order_by('-id').first()
        if last_record:
            return last_record.id + 1
        else:
            return 1

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.get_next_code()
        super().save(*args, **kwargs)
