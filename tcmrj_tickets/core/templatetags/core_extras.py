from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_groups')
def has_groups(user, group_name):
    groups = group_name.split(",")
    group = Group.objects.filter(name__in=groups)
    return True if all(item in group for item in user.groups.all()) else False