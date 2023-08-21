from django.http import HttpRequest
from django.shortcuts import render

from contact import models


def create(request: HttpRequest):

    context = {}

    return render(
        request,
        'contact/create.html',
        context,
    )
