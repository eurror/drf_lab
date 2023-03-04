from django.contrib import admin

from .models import User, Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_active", "is_mentor", "first_name", "last_name")
    list_editable = ("is_active", "is_mentor")
    search_fields = ("username", "email", "first_name", "last_name")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "competence", "linkedin")
    list_filter = ("language", "competence")
    