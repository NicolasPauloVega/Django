from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

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
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    create_date = models.DateField()

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
