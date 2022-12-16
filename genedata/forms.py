from django import forms
from django.forms import ModelForm
from .models import *

class ECForm(forms.Form):
    ec_name = forms.CharField(label='EC Name', max_length=100)

class GeneForm(ModelForm):
    class Meta:
        model = Gene 
        fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon', 'sequencing', 'ec']
