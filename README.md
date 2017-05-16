Exemplos do curso [Django para Iniciantes](https://www.youtube.com/playlist?list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd)
========================
* Autor: César Magalhães
* Tecnologias: Python 3.5.2, Django 1.11, MySQL 14.14
* Resumo: Django para Iniciantes
* Linguagens: Python
* Fonte: <https://github.com/cams7/exemplos-django-mixincode>
* Linkedin: <https://br.linkedin.com/in/cams7>

Qual a finalidade desses exemplos?
-------------------
Esses exemplos foram estudados e testados com intuíto de aprender um pouco mais sobre o Framework Django.

Sistemas requeridos
-------------------
* [Microsoft Windows 10](https://www.microsoft.com/pt-br/software-download/windows10)
* [Ubuntu 16.04.5 LTS](http://releases.ubuntu.com/16.04/)
* [Git](https://git-scm.com/downloads)
* [MySQL](https://www.mysql.com/)
* [PyCharm](https://www.jetbrains.com/pycharm/)

Para testa todos os exemplos
-------------------
* Instale o Git
* Instale o Mysql
* Instale o PyCharm Community

Exemplos do curso [Django para Iniciantes](https://www.youtube.com/playlist?list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd)
-------------------
01. [Aula 1](https://www.youtube.com/watch?v=ZJKNbgq_lhg&index=1&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd)
```sh
sudo apt-get install build-essential #Instala as biliotecas de C e C++
sudo apt-get install python-virtualenv #Cria ambiente distintos em Python 2 (Instala o PIP automaticamente)
sudo apt-get install python3-virtualenv #Cria ambiente distintos em Python 3

sudo apt-get install python3-mysqldb

sudo pip install --upgrade virtualenv
pip freeze | grep Django

cd ~
mkdir -P Dev/Python/Youtube/Mixincode
cd Dev/Python/Youtube/Mixincode

mkdir python3-env

virtualenv --python=/usr/bin/python3.5 --system-site-packages python3-env/django-1.11
source python3-env/django-1.11/bin/activate
pip install django

python --version

python
```
```py
import django
django.VERSION
exit()
```

```sh
mkdir Projects
cd Projects
django-admin.py startproject cursodjango2
cd cursodjango2
./manage.py runserver
#CTR-C
```
02. [Aula 2](https://www.youtube.com/watch?v=fOPGFMJUx0k&index=2&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd)
```sh
mysql --version
mysql -u root -p
CREATE DATABASE cursodjango2;
GRANT ALL PRIVILEGES ON cursodjango2.* TO 'mixincode'@'%';
FLUSH PRIVILEGES;
exit
mysql --host=127.0.0.1 --user=mixincode --password=django cursodjango2
exit

./manage.py check
./manage.py migrate

./manage.py shell
```
```py
from django.contrib.auth.models import User
usuario = User.objects.create_user('cams7', 'ceanma@gmail.com', '12345')
usuario.first_name = 'César'
usuario.last_name = 'Magalhães'
usuario.is_superuser = True
usuario.is_staff = True
usuario.save()
exit()
```

```sh
./manage.py runserver
#CTR-C

./manage.py shell
```
```py
from django.conf import settings
settings.DEBUG
settings.PROJECT_PATH
settings.BASE_DIR
settings.LANGUAGE_CODE
settings.TIME_ZONE
settings.MEDIA_ROOT
settings.MEDIA_URL
settings.STATIC_ROOT
settings.STATIC_URL
settings.STATICFILES_DIRS
settings.STATICFILES_FINDERS
settings.TEMPLATE_LOADERS
settings.TEMPLATES
exit()
```
03. [Aula 3](https://www.youtube.com/watch?v=G-m2PYLT61s&index=3&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd) | [aula3](https://github.com/cams7/exemplos-django-mixincode/tree/master/aula3)
```sh
./manage.py startapp aula3

./manage.py runserver
#http://localhost:8000/aula3/
#http://localhost:8000/aula3/ceanma@gmail.com/
#CTR-C

./manage.py shell
```
```py
from django.core.urlresolvers import reverse
reverse('aula3_index')
reverse('aula3_detail',args=['ceanma@gmail.com'])
exit()
```
04. [Aula 4](https://www.youtube.com/watch?v=dmtxcrNPqrs&index=4&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd) | [aula4](https://github.com/cams7/exemplos-django-mixincode/tree/master/aula4)
```sh
./manage.py startapp aula4

./manage.py shell
```
```py
from django import template
t = template.Template('Meu nome é {{nome|upper}}.')
c = template.Context({'nome': 'César A. Magalhães'})
t.render(c)
c = template.Context({'nome': 'Antônio O. Alves'})
t.render(c)

template_string = '''
{%if idade <= 20%}
A idade é menor ou igual a 20
{%else%}
A idade é maior que 20
{%endif%}
'''
t = template.Template(template_string)
c = template.Context({'idade': 20})
t.render(c)

c = template.Context({'idade': 34})
t.render(c)

exit()
```

```sh
./manage.py runserver
#http://localhost:8000/aula4
#CTR-C
```
05. [Aula 5](https://www.youtube.com/watch?v=qeI-ryYABbo&index=5&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd) | [aula5](https://github.com/cams7/exemplos-django-mixincode/tree/master/aula5)
```sh
./manage.py startapp aula5

./manage.py check
./manage.py makemigrations
./manage.py migrate

./manage.py shell
```
```py
from datetime import date
from aula5.models import Contato
contato = Contato()
contato.nome = 'César Antônio de Magalhães'
contato.email = 'ceanma@gmail.com'
contato.twitter = 'https://twitter.com/_cams7_'
contato.data_nascimento = date(1983,3,5)
contato.save()
exit()
```

```sh
./manage.py shell
```
```py
from aula5.models import Contato
contato = Contato.objects.get()
contato
contato = Contato.objects.get(id=1)
contato
contato = Contato.objects.get(pk=1)
contato
contatos = Contato.objects.filter(nome='César Antônio de Magalhães')
contatos
contatos = Contato.objects.all()
contatos
exit()
```

```sh
./manage.py shell
```
```py
from aula5.models import Post, Categoria, Comentarios
categoria1 = Categoria(nome='Desenvolvimento web')
categoria1.save()
categoria2 = Categoria(nome='Sistemas distribuidos')
categoria2.save()
post1 = Post(titulo='Meu primeiro post', texto='Texto do meu primeiro post')
post1.save()
post1.categorias.add(categoria1)
post1.categorias.add(categoria2)
post1.categorias.all()
comentario1 = Comentarios(autor='César A. Magalhães', comentario='Meu comentário')
comentario1.post = post1
comentario1.save()
comentario2 = Comentarios(autor='César A. Magalhães', comentario='Meu segundo comentário')
comentario2.post = post1
comentario2.save()
exit()
```

```sh
./manage.py shell
```
```py
from aula5.models import Post, Categoria, Comentarios
categoria1 = Categoria.objects.get(id=1)
categoria1.posts.all()
post1 = Post.objects.get(id=1)
post1.categorias.all()

comentario1 = Comentarios.objects.get(id=1)
comentario1.post
post1 = Post.objects.get(id=1)
post1.comentarios.all()
exit()
```
06. [Aula 6](https://www.youtube.com/watch?v=yvnuWmCl55g&index=6&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd) | [aula6](https://github.com/cams7/exemplos-django-mixincode/tree/master/aula6)
```sh
./manage.py startapp aula6

./manage.py check
./manage.py makemigrations
./manage.py migrate

./manage.py runserver
#http://localhost:8000/aula6
#http://localhost:8000/aula6/1
#CTR-C
```
07. [Aula 7](https://www.youtube.com/watch?v=S-wR_jecgt4&index=7&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd) | [aula7](https://github.com/cams7/exemplos-django-mixincode/tree/master/aula7)
```sh
./manage.py startapp aula7

./manage.py shell
```
```py
from django.contrib.auth.models import User
usuario = User.objects.create_user('luiz', 'luiz@teste.com', 'abc123')
usuario.username
usuario.email
usuario.is_superuser
usuario.first_name = 'Luiz'
usuario.last_name = 'Gomes'
usuario.save()
usuario.set_password('12345')
usuario.save()
exit()
```

```sh
./manage.py check
./manage.py makemigrations
./manage.py migrate

./manage.py shell
```
```py
from django.conf import settings
settings.AUTH_PROFILE_MODULE
settings.LOGIN_URL
exit()
```

```sh
./manage.py shell
```
```py
from datetime import date
from aula7.models import UserProfile
from django.contrib.auth.models import User
usuario = User.objects.get(username='cams7')
perfil = UserProfile.objects.create(user=usuario)
perfil.birthday=date(1983,3,5)
perfil.save()
exit()
```

```sh
./manage.py shell
```
```py
from django.contrib.auth.models import User, Permission
usuario = User.objects.get(id=2)
usuario.user_permissions.all()
permissoes = Permission.objects.all()
permissoes
usuario.user_permissions.add(permissoes[3])
usuario.user_permissions.all()
exit()
```

```sh
./manage.py runserver
#http://localhost:8000/aula7
#http://localhost:8000/aula7/sair
#http://localhost:8000/view_protegida
#http://localhost:8000/view_protegida2
#CTR-C


./manage.py shell
```
```py
from django.contrib.auth.models import User, Group, Permission
usuario = User.objects.create_user('luan', 'luan@teste.com', '12345')
usuario.first_name = 'Luan'
usuario.last_name = 'Silva'
usuario.save()
usuario.user_permissions.all()
usuario.user_permissions.clear()
usuario.user_permissions.all()
grupos = Group.objects.all()
grupos
grupo = Group.objects.create(name='Grupo 1')
grupo
grupo.permissions.all()
permissoes = Permission.objects.all()
grupo.permissions.add(permissoes[3])
grupo.permissions.all()
usuario.groups.all()
usuario.groups.add(grupo)
usuario.groups.all()
exit()
```

```sh
./manage.py runserver
#CTR-C
```
08. [Aula 8](https://www.youtube.com/watch?v=l1KHe-DQ6UI&index=8&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd) | [aula8](https://github.com/cams7/exemplos-django-mixincode/tree/master/aula8)
```sh
./manage.py startapp aula8

./manage.py check
./manage.py makemigrations
./manage.py migrate

./manage.py runserver
#http://localhost:8000/admin/aula8/contact/
#CTR-C
```
09. [Aula 9](https://www.youtube.com/watch?v=69S6X9zy7xQ&index=9&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd&t=2537s) | [aula9](https://github.com/cams7/exemplos-django-mixincode/tree/master/aula9)
```sh	
./manage.py startapp aula9

./manage.py runserver
#http://localhost:8000/aula9
#CTR-C

./manage.py test aula9

./runtests
```
10. [Aula 10](https://www.youtube.com/watch?v=La58UNoU_dY&index=10&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd) | [aula10](https://github.com/cams7/exemplos-django-mixincode/tree/master/aula10)
```sh	
./manage.py startapp aula10

./manage.py collectstatic

./manage.py runserver
#http://localhost:8000/aula10
#CTR-C
```
11. [Aula 11](https://www.youtube.com/watch?v=GKeR8BZRX-A&index=11&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd) | [aula11](https://github.com/cams7/exemplos-django-mixincode/tree/master/aula11)
12. [Aula 12](https://www.youtube.com/watch?v=xx0D44dnzy4&index=12&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd) | [aula12](https://github.com/cams7/exemplos-django-mixincode/tree/master/aula12)
13. [Aula 13](https://www.youtube.com/watch?v=HXIdtcDMUAI&index=13&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd) | [aula13](https://github.com/cams7/exemplos-django-mixincode/tree/master/aula13)
14. [Aula 14](https://www.youtube.com/watch?v=UkY9dvYFQ_E&index=14&list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd) | [aula14](https://github.com/cams7/exemplos-django-mixincode/tree/master/aula14)

