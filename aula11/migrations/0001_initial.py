# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 14:16
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado')),
            ],
            options={
                'verbose_name': 'Categoria',
                'ordering': ['name'],
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('body', models.TextField(verbose_name='Texto')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='aula11.Category', verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'ordering': ['-created_on'],
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField(default=0, verbose_name='Idade')),
            ],
            options={
                'verbose_name': 'User info',
                'verbose_name_plural': 'User infos',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
            ],
            options={
                'ordering': ['-username'],
                'indexes': [],
                'proxy': True,
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Postado por'),
        ),
    ]
