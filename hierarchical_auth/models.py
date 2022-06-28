from django.db import models

from django.contrib.auth.models import Group

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except:
    from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModelBase

# enhance Group class by adding a parent field needed by mptt

models.ForeignKey(
    Group,
    null            = True,
    blank           = True,
    on_delete       =  models.PROTECT, # added GT-220628
    related_name    = 'children',
    verbose_name    = _('parent'),
    help_text       = _('The group\'s parent group. None, if it is a root node.')
).contribute_to_class(Group, 'parent')

MPTTModelBase.register(Group, order_insertion_by=['name'])

# enhance User class by adding a new method that returns all groups

def get_all_groups(self, only_ids=False):
    """
    Returns all groups the user is member of AND all descendants groups of those
    groups.
    """
    direct_groups = self.groups.all()
    groups = set()
    # which direction should we really use the graph?
    for group in direct_groups:
        ancestors = group.get_ancestors(include_self=True).all()
        for ancestor in ancestors:
            if only_ids:
                groups.add(ancestor.id)
            else:
                groups.add(ancestor)
    return groups
    for group in direct_groups:
        descendants = group.get_descendants(include_self=True).all()
        for descendant in descendants:
            if only_ids:
                groups.add(descendant.id)
            else:
                groups.add(descendant)
    return groups

User.add_to_class('get_all_groups', get_all_groups)

