# Generated by Django 5.0.3 on 2024-04-05 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_alter_article_id_alter_category_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['id'], 'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to='articles', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='article',
            name='public',
            field=models.BooleanField(verbose_name='¿Publicado?'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='category',
            name='create_date',
            field=models.DateField(verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=110, verbose_name='Nombre'),
        ),
    ]