from django import template
from tyytiki.models import *

register = template.Library()


@register.simple_tag(name='get_cats')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('tyytiki/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}