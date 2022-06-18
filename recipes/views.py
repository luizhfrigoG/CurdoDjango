# from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Luiz Henrique',
    })


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(request):
    return HttpResponse('sobre')
