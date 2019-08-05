from django import template

register = template.Library()

@register.filter(is_safe=True)
def capital(username):
    username.capitalize()
