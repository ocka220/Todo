from django.contrib import admin

from list_item.models import ListItemModel


class ListItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'priority', 'listmodel_id']
    list_filter = ['created', 'name', 'is_done', 'listmodel_id']
    search_fields = ['name', 'listmodel_id']


admin.site.register(ListItemModel, ListItemAdmin)
