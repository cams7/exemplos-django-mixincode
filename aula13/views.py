# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from aula13.forms import UploadFileForm
"""
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse('aula13_index'))
    else:
        form = UploadFileForm()

    return render(request, 'aula13/index.html',
        {'form': form}
    )

def handle_uploaded_file(file):
    destination = open('/tmp/%s' %file.name, 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()
"""
"""
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('aula13_index'))
    else:
        form = UploadFileForm()

    return render(request, 'aula13/index.html',
        {'form': form}
    )
"""

def index(request):
    if request.session.get('view_this_page', False):
        visitou = True
    else:
        visitou = False
        request.session['view_this_page'] = True
    return render(request, 'aula13/index.html',
        {'visitou': visitou}
    )