from django import template

register = template.Library()

@register.filter(name='progress_bar')
def progress_bar(number):
    MAX_LENGTH = 20  # Longitud máxima de la barra de progreso
    filled_length = int(MAX_LENGTH * number / 100)  # Longitud de la barra llena

    bar = '[' + '=' * filled_length + ' ' * (MAX_LENGTH - filled_length) + ']'
    percentage = f'{number}%'

    return f'{bar} {percentage}'
