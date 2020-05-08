from django.contrib import admin
from .models import Cerita, SubCategories, Categories

@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ("title", "deskripsi", "image_sub_categories", "active")
    search_fields = ("title","deskripsi")
    prepopulated_fields = {"slug":("title",)}

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("title", "deskripsi", "active", "image_categories")
    search_fields = ("title", "deskripsi")
    prepopulated_fields = {"slug":("title",)}

@admin.register(Cerita)
class CeritaAdmin(admin.ModelAdmin):
    list_display = ("judul", "chapter", "status", "image_cover", "date_created", "date_updated")
    search_fields = ("judul", "chapter", "status")
    prepopulated_fields = {"slug":("judul",)}
    autocomplete_fields = ("categories", "sub_categories")
    list_filter = ("judul", "date_created", "date_updated", "status")
    list_editable = ("status",)
