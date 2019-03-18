# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUsrAdmin

from .models import User


class UserAdmin(DjangoUsrAdmin):
    search_fields = ("email",)
    list_display = ("username", "email", "is_active", "is_superuser")
    list_filter = ("is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email", "first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_superuser",
                    "is_staff",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    ordering = ("id",)


admin.site.register(User, UserAdmin)
