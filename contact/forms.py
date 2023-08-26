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
            'email', 'description', 'category',
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
        # print(cleaned_data)

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do erro',
                    code='invalid'  # erros que podem ser criados
                )
            )

        return first_name