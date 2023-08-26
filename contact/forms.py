from typing import Any, Dict

from django import forms
from django.core.exceptions import ValidationError

from contact import models


class ContactForm(forms.ModelForm):

    # Recriando o campo
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class-a class-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro nome',
        help_text='Texo de ajuda do usuário'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Atualizar um widget já existente
        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'class-a class-b',
        #     'placeholder': 'Aqui veio do init',
        # })

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
        # Criar um novo widget
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'escreva aqui'
        #         }
        #     )
        # }

    def clean(self) -> Dict[str, Any]:
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'  # erros que podem ser criados
            )
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'  # erros que podem ser criados
            )
        )
        return super().clean()
