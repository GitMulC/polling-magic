from django.contrib import admin
from .models import Poll
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Poll)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('set',)}
    list_filter = ('release_date',)
    list_display = ('set', 'release_date',)
    search_fields = ['set', 'lore']
    summernote_fields = ('lore')
