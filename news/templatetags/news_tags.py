from django import template
from django.db.models import Count, Q
from news.models import Categories

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Categories.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Hello', arg2='world'):
    categories = Categories.objects.filter(Q(news__pk__gt=0) & Q(news__is_published=True)).annotate(cnt=Count('news'))
    # categories = Categories.objects.all()
    return {"categories": categories, "arg1": arg1, "arg2": arg2}
