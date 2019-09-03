from django.db import models
from .settings import ASCENDING_STRATEGY
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModelBase

User = get_user_model()

# enhance Group class by adding a parent field needed by mptt

models.ForeignKey(
    Group,
    null            = True,
    blank           = True,
    related_name    = 'children',
    verbose_name    = _('parent'),
    help_text       = _('The group\'s parent group. None, if it is a root node.'),
    on_delete=models.CASCADE,
).contribute_to_class(Group, 'parent')

MPTTModelBase.register(Group, order_insertion_by=['name'])

# enhance User class by adding a new method that returns all groups


def get_all_groups(self, only_ids=False, ascending_strategy=ASCENDING_STRATEGY):
    """
    Returns all groups the user is member of AND all descendants groups of those
    groups.
    """
    direct_groups = self.groups.all()
    groups = set()
    # which direction should we really use the graph?
    if ascending_strategy:
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

