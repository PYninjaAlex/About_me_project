from django.contrib import admin
from .models import AboutMeDatabase


@admin.register(AboutMeDatabase)
class Database(admin.ModelAdmin):
    list_display = ("name", "second_name", "age")
