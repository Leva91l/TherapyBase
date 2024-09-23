from django import template
from therapyapp.models import *

register = template.Library()


@register.inclusion_tag('tags/sidebar.html')
def sidebar():
    directions = Direction.objects.all()
    return {'directions': directions}

@register.inclusion_tag('tags/footer.html')
def footer():
    contacts = Worker.objects.all()
    return {'contacts': contacts}
