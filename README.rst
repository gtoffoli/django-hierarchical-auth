========================
django-hierarchical-auth
========================

django-hierarchical-auth provides extended functionality for the default User
/ Group permissions system in Django.

It allows to hierarchically organize the groups, allowing easy permissions
management for complex systems.

Ascending or Descending strategy
--------------------------------

Depending on how you expect to build your hierarchy, when trying to get
(`user.get_all_groups`) all groups a user belong to including up to the root
it might require going through the ancestors or the decendants of the direct
groups.

Since I currently have no reason to push one strategy or the other, a settings

`HIERARCHICAL_AUTH_STRATEGY_ASCENDING` (defaults to `True`) is used to pilot
the default behaviour for `get_all_groups`

It's possible to force an additional parameter `False` to the method to get the
groups the other way around.

Usage
=====

As it's built on top of django.contrib.auth all you need to do is install it.

Updates
=======

0.4
---

 * Little cleanup with the descendant vs. ascendant logic


0.3
---

 * Now working with django 1.5 and 1.6, *including custom user models*!
 * Updated for MPTT>1.5.
