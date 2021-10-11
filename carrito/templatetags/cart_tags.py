from django import template


register = template.Library()


@register.filter()

def multiply(value,arg):
    subtotal = float(value) * arg
    total = round(subtotal,2)
    return total

@register.filter()

def money_format(value,arg):
    return f'{value}{arg}'


