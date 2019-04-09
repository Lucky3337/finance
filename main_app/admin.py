from django.contrib import admin
from .models import Category, Post, Document, Image
from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'text'


admin.site.register(Category)
admin.site.register(Post, SomeModelAdmin)
admin.site.register(Document)
admin.site.register(Image)
