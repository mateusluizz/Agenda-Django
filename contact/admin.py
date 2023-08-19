from django.contrib import admin

from contact import models

# https://docs.djangoproject.com/en/4.2/ref/contrib/admin/


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'show',)
    ordering = ('-id',)
    list_filter = ('created_date',)
    search_fields = ('id', 'first_name', 'last_name', 'phone')
    list_per_page = 20
    list_max_show_all = 100
    list_editable = ('first_name', 'last_name', 'show',)
    list_display_links = ('id', 'phone')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    ordering = ('-id',)
