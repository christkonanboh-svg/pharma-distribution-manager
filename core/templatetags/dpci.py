from django import template

register = template.Library()


@register.filter
def fcfa(value):
    try:
        number = int(round(float(value)))
    except (TypeError, ValueError):
        return value
    return f"{number:,}".replace(",", " ") + " F"


@register.filter
def initials(value):
    parts = [part for part in str(value).replace("-", " ").split() if part]
    if not parts:
        return "DP"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()


@register.filter
def percent(value):
    try:
        return f"{int(value)} %"
    except (TypeError, ValueError):
        return value
