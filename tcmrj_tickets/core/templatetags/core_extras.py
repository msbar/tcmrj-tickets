from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_groups')
def has_groups(user, group_name):
    group = Group.objects.filter(name__in=[group_name])
    return True if all(item in user.groups.all() for item in group) else False