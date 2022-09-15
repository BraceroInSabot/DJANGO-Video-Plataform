from django import forms

from core.models import *

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["url",]
        labels = {"url": "YOUTUBE URL",}

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label="Search on plataform")