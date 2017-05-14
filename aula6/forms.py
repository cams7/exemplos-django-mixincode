# -*- coding: utf-8 -*-
from django import forms

from aula6.models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        exclude = ['id']
