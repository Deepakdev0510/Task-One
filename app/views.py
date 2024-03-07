# views.py
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import URLShorteningForm
from .models import ShortenedURL

def shorten_url(request):
    if request.method == 'POST':
        form = URLShorteningForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            shortened_url = ShortenedURL(original_url=original_url)
            shortened_url.save()
            return render(request, 'app/shortened.html', {'shortened_url': shortened_url})
    else:
        form = URLShorteningForm()
    return render(request, 'app/shorten.html', {'form': form})

def redirect_to_original(request, short_url):
    try:
        shortened_url = ShortenedURL.objects.get(short_url=short_url)
        return redirect(shortened_url.original_url)
    except ShortenedURL.DoesNotExist:
        raise Http404
