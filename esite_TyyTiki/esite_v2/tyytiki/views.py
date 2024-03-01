from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from .models import *

menu = [{'title': 'Серьги'},
        {'title': 'Воротники'},
        {'title': 'Подвески'},
        {'title': 'Броши'}
        ]


def index(request):
    prods = Product.objects.all()

    context = {'prods': prods,
               'menu': menu,
               'title': 'Главная страница',
               }

    return render(request, 'tyytiki/index.html', context=context)


def about(request):
    prods = Product.objects.all()
    cats = Category.objects.all()
    context = {'prods': prods,
               'cats': cats,
               'menu': menu,
               'title': 'Главная страница',
               }
    return render(request, 'tyytiki/about.html', context=context)


def delivery(request):
    prods = Product.objects.all()
    cats = Category.objects.all()
    context = {'prods': prods,
               'cats': cats,
               'menu': menu,
               'title': 'Главная страница',
               }
    return render(request, 'tyytiki/delivery.html', context=context)


def show_prod(request, prod_id):
    post = get_object_or_404(Product, slug=prod_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    prods = Product.objects.filter(cat_id=cat_id)
    context = {'prods': prods,
               'menu': menu,
               'title': 'Отображение по рубрикам',
               'cat_selected': cat_id}

    return render(request, 'tyytiki/products.html', context=context)


def all_products(request):
    prods = Product.objects.all()
    cats = Category.objects.all()

    context = {'prods': prods,
               'cats': cats,
               'menu': menu,
               'title': 'Изделия',
               'cat_selected': 0,
               }

    return render(request, 'tyytiki/products.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
