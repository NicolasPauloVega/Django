from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('create_date','update_date')
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

#Configurar el titulo del Panel
title="Master Blog de Articulos"
admin.site.site_header=title
admin.site.site_title=title
admin.site.index_title="Panel de Gestión"