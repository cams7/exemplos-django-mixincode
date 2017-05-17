# -*- coding: utf-8 -*-
from django import forms

from aula13.models import UploadFile


class UploadFileForm(forms.ModelForm):
    """
    title = forms.CharField(max_length=50,required=True)
    #file = forms.FileField(required=True)
    file = forms.ImageField(required=True)
    """

    class Meta:
        model = UploadFile
        exclude = ['id']


