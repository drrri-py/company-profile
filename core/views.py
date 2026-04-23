from django.shortcuts import render, get_object_or_404
from .models import Product, Article, Gallery, CompanyProfile

def get_profile():
    return CompanyProfile.load()

def home(request):
    profile = get_profile()
    recent_articles = Article.objects.order_by('-created_at')[:3]
    featured_products = Product.objects.all()[:3]
    return render(request, 'core/home.html', {
        'profile': profile,
        'recent_articles': recent_articles,
        'featured_products': featured_products,
    })

def profile_view(request):
    profile = get_profile()
    return render(request, 'core/profile.html', {'profile': profile})

def product_list(request):
    profile = get_profile()
    products = Product.objects.all()
    return render(request, 'core/products.html', {'profile': profile, 'products': products})

def article_list(request):
    profile = get_profile()
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'core/articles.html', {'profile': profile, 'articles': articles})

def article_detail(request, slug):
    profile = get_profile()
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'core/article_detail.html', {'profile': profile, 'article': article})

def gallery_view(request):
    profile = get_profile()
    galleries = Gallery.objects.all()
    return render(request, 'core/gallery.html', {'profile': profile, 'galleries': galleries})

def contact_view(request):
    profile = get_profile()
    return render(request, 'core/contact.html', {'profile': profile})
