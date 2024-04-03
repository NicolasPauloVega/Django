from django import template

register = template.Library()

@register.filter(name='textoAlreves')
def textoAlreves(value):
    return value[::-1]
