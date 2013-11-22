from django.contrib import admin

from .models import ShortenedUrl


class ShortenedUrlAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'original',
        'shortened',
        'created',
        'modified',
    ]

admin.site.register(ShortenedUrl, ShortenedUrlAdmin)
