# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    image = forms.FileField(
        label='Select a file'
    )
    image_class = forms.CharField(label='Enter Image class')
    text = forms.CharField(label='Enter Image Text')