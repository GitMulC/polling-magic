from django.contrib import admin
from .models import Poll
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Poll)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('lore')
