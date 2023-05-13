from django.shortcuts import render

from contact import models


def index(request):
    contacts = models.Contact.objects \
        .filter(show=True) \
        .order_by('-id')[:25]

    # print(contacts.query)  # consulta SQL

    context = {
        'contacts': contacts
    }

    return render(
        request,
        'contact/index.html',
        context
    )
