from django.contrib import admin
from .models import UserModel, Saldo, AuditEntry
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as ProfileBukuAdmin
from django.db.models import Sum
import datetime


class DateYearFilter(admin.SimpleListFilter):
    title = 'year'
    parameter_name = "date_updated"

    def lookups(self, request, model_admin):
        firstyear = UserModel.objects.order_by("date_updated").first().date_updated.year
        currentyear = datetime.datetime.now().year
        years = []
        for x in range(currentyear - firstyear):
            yearloop = firstyear+x
            years.insert(0,(str(currentyear), str(yearloop)))
        years.insert(0,(str(currentyear), str(currentyear)))
        return years

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(date_updated__year=self.value())
        else:
            return queryset

@admin.register(UserModel)
class UserAdmin(ProfileBukuAdmin):
    fieldsets = (
        (None, {"fields":("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "username_user","slug", "no_telepon", "alamat", "biografi", "gender", 'saldo')},),
        ("Personal Picture", {"fields": ("image_profile", "image_walpaper",)},),
        ("Permission", {"fields":("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},),
        ("Important date", {"fields": ("last_login", "date_joined")},),
    )
    
    add_fieldsets = (
        (None, {"classes":("wide",),"fields":("email", "password1", "password2"),},),
    )


    list_filter = ("is_staff", "is_superuser", "is_active",DateYearFilter, "gender")
    list_display_links = ("email",)
    list_editable = ("gender",)
    prepopulated_fields = {"slug": ("username_user",)}
    date_hierarchy = "date_updated"
    list_display = ("img_profile","email", "username_user", "gender", "slug","is_staff","date_updated" , "last_login",)
    search_fields = ("email", "first_name", "last_name", "username_user", "alamat", "date_updated", "gender",)
    ordering = ("email",)

    def img_profile(self, obj):
        if obj.image_profile:
            return format_html(
                '<img src="%s" width="100" heigth="100" />' % obj.image_profile.url
            )
        return ""
    img_profile.short_description = "Usermodel"

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.has_perm('usermodels.read_user'):
            return [f.email for f in self.model._meta.fields]




@admin.register(Saldo)
class SaldoAdmin(admin.ModelAdmin):
    list_display = ("date_created", "date_updated")


@admin.register(AuditEntry)
class AuditEntryAdmin(admin.ModelAdmin):
    list_display = ['action', 'username', 'ip',]
    list_filter = ['action',]