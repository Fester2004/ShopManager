from django.http import HttpResponse
from django.shortcuts import render
from First.models import Shop


def index(request):

    ctx = {
        'shops': Shop.objects.all()
    }
    return render(request, "index.html", context=ctx)