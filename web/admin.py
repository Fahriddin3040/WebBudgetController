from django.contrib import admin
from web.models import User, Note


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'f_name', 'l_name', 'category_id')
    list_display_links = ('id', 'f_name', 'l_name', 'category_id')
    search_fields = ('f_name', 'l_name')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'sort', 'reason', 'price', 'date_time')
    list_display_links = ('id', 'user_id', 'sort', 'reason', 'price', 'date_time')
    search_fields = ('reason', 'date_time')


