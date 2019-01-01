from django import template

register = template.Library()

@register.filter(name='cut') #This is how to register our own custom filter with Decorator

def cut(value,arg):
    """
    This cuts out all value of "arg" from the string!
    """
    return value.replace(arg,'')

#register.filter('cut',cut) #This is how to register our own custom filter with alternate way