from django import template
from therapyapp.models import *

register = template.Library()


@register.inclusion_tag('tags/sidebar.html')
def sidebar():
    directions = Direction.objects.all()
    return {'directions': directions}
