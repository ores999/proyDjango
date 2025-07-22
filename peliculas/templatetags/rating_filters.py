from django import template
register = template.Library()

@register.filter
def rating_class(value):
    try:
        v = float(value)
    except (TypeError, ValueError):
        return 'rating-unk'
    if v >= 8:      return 'rating-good'
    if v >= 5:      return 'rating-mid'
    return 'rating-bad'
