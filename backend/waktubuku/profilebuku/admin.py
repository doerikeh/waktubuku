from django.contrib import admin
from .models import ProfileWBModel, UserModel, Saldo
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as ProfileBukuAdmin
from django.db.models import Sum

@admin.register(UserModel)
class UserAdmin(ProfileBukuAdmin):
    fieldsets = (
        (None, {"fields":("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")},),
        ("Permission", {"fields":("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},),
        ("Important date", {"fields": ("last_login", "date_joined")},),
    )
    
    add_fieldsets = (
        (None, {"classes":("wide",),"fields":("email", "password1", "password2"),},),
    )

    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


@admin.register(ProfileWBModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("img_profile", "date_created", "date_updated", "gender")
    search_fields = ("alamat", "gender")
    date_hierarchy = "date_created"
    list_filter = ("gender", "date_created", "date_updated")
    list_editable = ("gender",)
    prepopulated_fields = {"slug": ("user",)}


    def img_profile(self, obj):
        if obj.image_profile:
            return format_html(
                '<img src="%s" width="100" heigth="100" />' % obj.image_profile.url
            )
        return ""
    img_profile.short_description = "Profile"




@admin.register(Saldo)
class SaldoAdmin(admin.ModelAdmin):
    list_display = ("date_created", "date_updated")
