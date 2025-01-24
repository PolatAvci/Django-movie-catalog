from django.contrib import admin
from .models import Movies


class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_date", "isPublished", "isHome")
    list_display_links = ("id", "name")
    list_filter = ("created_date",)
    list_editable = ("isPublished","isHome")
    search_fields = ("name", "description")
    list_per_page = 20
    
# Register your models here.
admin.site.register(Movies, MovieAdmin)