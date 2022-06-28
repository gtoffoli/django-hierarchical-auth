from django.contrib import admin
from django.conf import settings
# from django.db.models import get_model # commented GT-220628

# from models import Group, User  # this takes care of custom users Etc.
from django.contrib.auth.models import Group, User # GT-220628
from django.contrib.auth.admin import GroupAdmin

try:
    module_name, class_name = settings.AUTH_USER_ADMIN_CLASS.rsplit('.', 1)
    mod = __import__(module_name, fromlist=[class_name])
    UserAdmin = getattr(mod, class_name)
except:
    from django.contrib.auth.admin import UserAdmin

UserChangeForm = UserAdmin.form

from mptt.forms import TreeNodeMultipleChoiceField

if getattr(settings, 'MPTT_USE_FEINCMS', False):
    from mptt.admin import FeinCMSModelAdmin
    class GroupMPTTModelAdmin(GroupAdmin, FeinCMSModelAdmin):
        pass
else:
    from mptt.admin import MPTTModelAdmin
    class GroupMPTTModelAdmin(GroupAdmin, MPTTModelAdmin):
        pass

admin.site.unregister(Group)
admin.site.register(Group, GroupMPTTModelAdmin)

class UserWithMPTTChangeForm(UserChangeForm):
    groups = TreeNodeMultipleChoiceField(queryset=Group.objects.all())

class UserWithMPTTAdmin(UserAdmin):
    form = UserWithMPTTChangeForm

admin.site.unregister(User)
admin.site.register(User, UserWithMPTTAdmin)
