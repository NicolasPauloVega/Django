from django import template

register = template.Library()

@register.filter(name='emojify')
def emojify(value):
    # Diccionario de palabras clave y sus emojis correspondientes
    emoji_mapping = {
        'feliz': '😀',
        'triste': '😢',
        'sorpresa': '😲',
        'enojado': '😠',
        'amor': '❤️',
        'risa': '😂',
        'llanto': '😭',
        'miedo': '😨',
        'enojado': '😡',
        'sueño': '😴',
        'confundido': '😕',
        'enfermo': '🤒',
        'cansado': '😫'
    }

    # Reemplazar palabras clave con emojis
    for keyword, emoji in emoji_mapping.items():
        value = value.replace(keyword, emoji)

    return value
