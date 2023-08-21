from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from contact import models


def index(request: HttpRequest):
    contacts = models.Contact.objects \
        .filter(show=True) \
        .order_by('-id')

    paginator = Paginator(contacts, 25)
    page_nummber = request.GET.get('page')
    page_obj = paginator.get_page(page_nummber)

    # print(contacts.query)  # consulta SQL

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos -'
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def search(request: HttpRequest):

    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = models.Contact.objects \
        .filter(show=True) \
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(email__icontains=search_value) |
            Q(phone__icontains=search_value)
        ) \
        .order_by('-id')

    paginator = Paginator(contacts, 25)
    page_nummber = request.GET.get('page')
    page_obj = paginator.get_page(page_nummber)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search -',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request: HttpRequest, contact_id: int):
    # single_contact = models.Contact.objects.filter(pk=contact_id).first()
    # single_contact = get_object_or_404(
    #     models.Contact.objects.filter(pk=contact_id)
    # )
    single_contact = get_object_or_404(
        models.Contact,
        pk=contact_id,
        show=True
    )

    if single_contact is None:
        raise Http404('Contact not found!')

    context = {
        'contact': single_contact,
        'site_title': f'{single_contact.first_name} {single_contact.last_name} -'
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
