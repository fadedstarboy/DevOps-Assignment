from django.contrib import admin

from app.models import GeeksModel


# Register your models here.
class GeeksModelAdmin (admin.ModelAdmin):
    list_display = [
        'id', 'title', 'description', 'last_modified'
    ]

admin.site.register(GeeksModel, GeeksModelAdmin)
