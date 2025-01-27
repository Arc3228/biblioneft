from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    list_display = (
        "phone",
        "name",
        "surname",
        "lastname",
        "date_of_birth",
        "education",
        "prof",
        "study_work",
        "passport",
        "given",
    )
    fieldsets = (
        (
            None,
            {"fields": ("phone", "password")},
        ),
        (
            "Personal info",
            {
                "fields": (
                    "name",
                    "surname",
                    "lastname",
                    "date_of_birth",
                    "education",
                    "prof",
                    "study_work",
                    "passport",
                    "given",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("phone", "name", "surname", "lastname")
    ordering = ("phone",)


admin.site.register(User, CustomUserAdmin)