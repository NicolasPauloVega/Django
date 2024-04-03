from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='null', upload_to="articles")
    public = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['id']

    def __str__(self):
        if self.public:
            publico = "(Publico)"
        else:
            publico = "(Privado)"
        return f"{self.id}-{self.title} : {publico}"