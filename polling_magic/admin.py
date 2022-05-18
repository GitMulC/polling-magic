from django.contrib import admin
from .models import Poll, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Poll)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('set',)}
    list_filter = ('release_date',)
    list_display = ('set', 'release_date',)
    search_fields = ['set', 'lore']
    summernote_fields = ('lore')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
