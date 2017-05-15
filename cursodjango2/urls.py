"""cursodjango2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from aula3.views import index as aula3_index
from aula3.views import detail as aula3_detail
from aula4.views import index as aula4_index
from aula6.views import index as aula6_index
from aula6.views import detail as aula6_detail
from aula7.views import index as aula7_index
from aula7.views import sair as aula7_sair
from aula7.views import view_protegida as aula7_view_protegida
from aula7.views import view_protegida2 as aula7_view_protegida2

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^aula3/$', aula3_index, name='aula3_index'),
    url(r'^aula3/(?P<username>[\w.@+-]+)/$', aula3_detail, name='aula3_detail'),

    url(r'^aula4/$', aula4_index, name='aula4_index'),

    url(r'^aula6/$', aula6_index, name='aula6_index'),
    url(r'^aula6/(?P<id>\d+)/$', aula6_detail, name='aula6_detail'),

    url(r'^aula7/$', aula7_index, name='aula7_index'),
    url(r'^aula7/sair/$', aula7_sair, name='aula7_sair'),
    url(r'^aula7/view_protegida/$', aula7_view_protegida, name='aula7_view_protegida'),
    url(r'^aula7/view_protegida2/$', aula7_view_protegida2, name='aula7_view_protegida2'),
]
