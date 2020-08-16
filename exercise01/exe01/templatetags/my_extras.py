from django import template

register = template.Library()

@register.filter(name="taglio")

def taglio(value,arg):
    """
    Taglia la substringa arg dalla stringa
    """
    return value.replace(arg,'')

@register.filter(name="grassetto")
def grassetto(value):
    """
    Taglia la substringa arg dalla stringa
    """
    return value.upper()

"""
register.filter('taglio',taglio)
"""
