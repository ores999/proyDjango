from django import template
register = template.Library()

@register.filter
def times(number):
    """
    3 → range(3)  ➜  para iterar en la plantilla
    """
    try:
        return range(int(number))
    except (TypeError, ValueError):
        return range(0)