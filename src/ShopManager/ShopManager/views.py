from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    ctx = {
        'comander':'Corde'
    }
    return render(request, "index.html", context=ctx)