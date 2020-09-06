from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['id', 'email', 'name', 'is_superuser', 'last_login']
  
    fieldsets = (
      (None, {'fields': ('email', 'password')}),
      ('Personal Info', {'fields': ('name',)}),
      ('Permissions',
          {
              'fields': (
                  'is_active',
                  'is_staff',
                  'is_superuser',
              )
          }
      ),
      ('Dates', {'fields': ('last_login',)}),
    )
  
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2')
        }),
    )

# register the model and tell Django to use the above UserAdmin
# class to format the pages:
admin.site.register(models.User, UserAdmin)