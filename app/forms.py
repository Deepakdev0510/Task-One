# forms.py
from django import forms
from .models import ShortenedURL

class URLShorteningForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['original_url']
