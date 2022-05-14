from django import forms
from .models import *

class MovieFormSearch(forms.Form):
    country = forms.ModelChoiceField(label='کشور', queryset=Country.objects.all(), required=False)
    category = forms.ModelChoiceField(label='ژانر', queryset=Category.objects.all(), required=False)
    artist = forms.CharField(label='بازیگر', max_length=64, required=False)
    director = forms.CharField(label='کارگردان', max_length=64, required=False)