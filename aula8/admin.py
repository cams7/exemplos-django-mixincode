# -*- coding: utf-8 -*-
from django.contrib import admin

from aula8.models import Contact, Phone
from aula8.forms import ContactForm


class PhoneInline(admin.StackedInline):
    model = Phone


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'birthday'
    list_filter = ('active',)
    list_display = ('name', 'birthday', 'active')
    search_fields = ['name', 'info']
    inlines = [
        PhoneInline,
    ]
    form = ContactForm


admin.site.register(Contact, ContactAdmin)
# admin.site.register(Phone)