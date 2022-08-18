from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Categories


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'content', 'category', 'photo', 'get_photo', 'created_at', 'updated_at', 'is_published')
    readonly_fields = ('get_photo', 'created_at', 'updated_at')
    save_on_top = False

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')

    get_photo.short_description = 'Фото'


class CategorysAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Categories, CategorysAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
