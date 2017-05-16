# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User

from aula11.models import Category, Post

def index(request):
    #post_list = Post.published_objects.all()
    post_list = Post.objects.filter(published = True)
    return render(request, 'aula11/index.html',
       {'post_list': post_list}
    )
