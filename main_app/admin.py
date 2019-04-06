from django.contrib import admin
from .models import Category, Post, Document, Image

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Document)
admin.site.register(Image)
