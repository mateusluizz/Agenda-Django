from django.http import HttpRequest
from django.shortcuts import render, redirect

from contact.forms import ContactForm


def create(request: HttpRequest):

    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        context = {
            'form': form,
        }

        if form.is_valid():
            # contact = form.save(commit=False) # Editar algo antes de salvar
            contact = form.save()
            contact.save()
            return redirect('contact:create')

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
