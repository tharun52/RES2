from django import template

register = template.Library()

@register.filter(name="divide")
def divide(value, arg):
    try:    
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError):
        return None

@register.filter(name="int_convert")
def int_convert(value):
    try:
        return int(value)
    except(TypeError):
        return None