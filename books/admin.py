from django.contrib import admin
from . import models

class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'publicated_at')
    search_fields = ('title', 'publicated_at')

admin.site.register(models.Book, BookModelAdmin)