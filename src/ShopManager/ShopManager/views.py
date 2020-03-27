from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    ctx = {
        'comander':'com'
    }
    return render(request, "index.html", context=ctx)