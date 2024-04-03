from django import forms 
from django.core import validators

class FormArticulo(forms.Form):
    title = forms.CharField(
        label="Titulo",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el Titulo',
                'class': 'titulo_from_article'
            }
        ),
        validators=[
            validators.MaxLengthValidator(40, 'El titulo es demasiado largo'),
            validators.RegexValidator('^[A-Za-z0-9 ]*$', 'El titulo esta mal digitado', 'invalid_title')
        ]
    )
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Ingrese el contenido Ya',
                'class': 'contenido_form_article',
                'id': 'contenido_form'
            }
        )
    )
    public_options = [(0, 'No'), (1, 'Si')]
    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices=public_options
    )

