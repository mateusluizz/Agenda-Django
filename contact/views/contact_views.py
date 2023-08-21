from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404, render

from contact import models


def index(request: HttpRequest):
    contacts = models.Contact.objects \
        .filter(show=True) \
        .order_by('-id')[:50]

    # print(contacts.query)  # consulta SQL

    context = {
        'contacts': contacts,
        'site_title': 'Contatos -'
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
