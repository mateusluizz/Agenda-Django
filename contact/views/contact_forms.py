from django.http import HttpRequest
from django.shortcuts import render

from contact import models


def create(request: HttpRequest):

    search = request.POST
    if request.method == "POST":
        print(request.method)
        print(search.get('first_name'))
        print(search.get('last_name'))
        print(search.get('password'))

    print(search)

    context = {}

    return render(
        request,
        'contact/create.html',
        context,
    )
