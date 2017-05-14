# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
    lista = [
        u'Allisson',
        u'João',
        u'Pedro'
    ]
    return render(request, 'aula4/index.html', {'lista': lista})
