from typing import Any, Dict

from django import forms
from django.core.exceptions import ValidationError

from contact import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )

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
