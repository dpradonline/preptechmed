from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import About, Scripture, Point, Introduction, Overview


class PointAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order', )
    search_fields = ('question', 'answer')
    ordering = ['order']


class CustomText(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'id': 'project_update_textarea'})}
    }


admin.site.register(Introduction)
admin.site.register(Overview)
admin.site.register(About)
admin.site.register(Point, PointAdmin)
admin.site.register(Scripture)
