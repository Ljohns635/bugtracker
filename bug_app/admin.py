from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from bug_app.models import CustomUser

OTHER_FIELD = (
    (None, {'fields': ('tagline',)}),
)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + OTHER_FIELD
    fieldsets = UserAdmin.fieldsets + OTHER_FIELD

admin.site.register(CustomUser, CustomUserAdmin)
