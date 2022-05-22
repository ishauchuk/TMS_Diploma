from django import template
from salon.models import Masters

register = template.Library()


@register.simple_tag(name='getmasters')
def get_masters():
    return Masters.objects.all()
