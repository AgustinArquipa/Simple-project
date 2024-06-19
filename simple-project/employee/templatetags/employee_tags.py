from django import template

register = template.Library()
print("Registro -> ", register)

def getattr(value, arg):
    """Returns the value of an attribute of an object."""
    return getattr(value, arg, None)