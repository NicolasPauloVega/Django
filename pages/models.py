from django.db import models

# Create your models here.
class Page(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    title = models.CharField(max_length=50, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    slug = models.CharField(unique=True, max_length=150, verbose_name="Url Amigable")
    visible = models.BooleanField(verbose_name="¿Visible?")
    create_pg = models.DateField(auto_now_add=True, verbose_name="Creado el")
    update_pg = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return f"{self.title} - Url Amigable: {self.slug}"

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