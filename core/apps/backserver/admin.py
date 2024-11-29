from django.contrib import admin

from core.apps.backserver.models import Method

@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)

admin.register(Method, MethodAdmin)