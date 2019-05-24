from django.contrib import admin
from .models import *
# Register your models here.
#
# class SearchAdmin(admin.ModelAdmin):
#     list_display = ['id', 'author', 'title', 'text', 'create', 'updated']
#     raw_id_fields = ['author']

admin.site.register(Road)
# admin.site.register(SearchAdmin)