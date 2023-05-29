from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('phone', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('phone', 'password', 'last_login')}),
        # ('Personal info', {'fields': ('first_name', 'last_name', 'avater', 'group',
        #  'phone', 'city', 'state', 'country', 'dob', 'last_donate')}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2'),
        }),
    )
    search_fields = ('phone',)
    ordering = ('phone',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
