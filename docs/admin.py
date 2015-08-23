from django.contrib import admin

from docs.models import HackerearthDoc


class HackerearthDocAdminModel(admin.ModelAdmin):
    fields = (
        'user', 'timestamp', 'title', 'slug', 'parent',
        'body', 'published', 'is_document'
    )
    ordering = ('id', )


admin.site.register(HackerearthDoc, HackerearthDocAdminModel)
