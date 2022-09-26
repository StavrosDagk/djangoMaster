from django.shortcuts import get_object_or_404, render

from .models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, 'core/landing.html', {'articles': articles})


def about(request):
    return render(request, 'core/about.html')


def detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'core/detail.html', {'article': article})
