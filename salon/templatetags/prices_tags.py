from django import template
from salon.models import Services

register = template.Library()


@register.simple_tag(name='getprices')
def get_prices():
    return Services.objects.all()
