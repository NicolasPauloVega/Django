from django import forms
from django.core import validators

class FormArticle(forms.Form):
    title = forms.CharField(
        label="Titulo",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el Titulo',
                'class': 'Titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$','El titulo esta mal digitado','invalid_title')
        ]
    )
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea
    )
    public_options = [(0,'No'),(1,'Si')]
    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices=public_options
    )