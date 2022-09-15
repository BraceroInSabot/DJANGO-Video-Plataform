from django import forms

from core.models import *

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "url", "youtube_id"]
        labels = {"youtube_id": "YouTube ID", "title": "Title", "url": "URL"}

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label="Search on plataform")