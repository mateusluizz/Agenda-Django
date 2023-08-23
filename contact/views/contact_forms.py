from django import forms
from django.http import HttpRequest
from django.shortcuts import render

from contact import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )


def create(request: HttpRequest):

    if request.method == 'POST':
        context = {
            'form': ContactForm(data=request.POST),
        }

        return render(
            request,
            'contact/create.html',
            context,
        )
    context = {
        'form': ContactForm(),
    }

    return render(
        request,
        'contact/create.html',
        context,
    )
