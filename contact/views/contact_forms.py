from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact import models
from contact.forms import ContactForm


def create(request: HttpRequest) -> HttpResponse:
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            # contact = form.save(commit=False) # Editar algo antes de salvar
            contact = form.save()
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'form': ContactForm(),
        'form_action': form_action
    }

    return render(
        request,
        'contact/create.html',
        context,
    )


def update(request: HttpRequest, contact_id: int) -> HttpResponse:
    contact = get_object_or_404(
        models.Contact, pk=contact_id, show=True
    )
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(data=request.POST, instance=contact)
        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            # contact = form.save(commit=False) # Editar algo antes de salvar
            contact = form.save()
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action
    }

    return render(
        request,
        'contact/create.html',
        context,
    )
