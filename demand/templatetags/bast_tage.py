from django import template
from ..models import Category

register = template.Library()


@register.simple_tag
def title(data='مطالبه جدید'):
    return data


@register.inclusion_tag("demand/partials/category_navbar.html")
def category_navbar():
    return {
        'category': Category.objects.all()
    }
