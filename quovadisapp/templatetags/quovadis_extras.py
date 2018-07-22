from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def split_black(value):
    return value.split('-')[0]


@register.filter
@stringfilter
def split_yellow(value):
    return value.split('-')[1]


@register.filter
def even_or_odd(num):
    return not num % 2 == 0


@register.filter
def slice_service(service, idx):
    return service[idx]


@register.filter
def format_price(price):
    return '{:0,.0f}'.format(price)


@register.filter
def split_space(name, idx):
    return name.split(' ')[idx]