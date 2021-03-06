# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('birthday', models.DateField(verbose_name='Aniversário')),
                ('info', models.TextField(blank=True, verbose_name='Informações do contato')),
                ('active', models.BooleanField(default=True, help_text='Marque para definir o contato como ativo.', verbose_name='Contato ativo')),
            ],
            options={
                'verbose_name_plural': 'Contatos',
                'verbose_name': 'Contato',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aula8.Contact', verbose_name='Contato')),
            ],
            options={
                'verbose_name_plural': 'Telefones',
                'verbose_name': 'Telefone',
            },
        ),
    ]
