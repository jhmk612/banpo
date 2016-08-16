from django.contrib import admin
from .models import People, Post, Comment, Like


# Register your models here.



admin.site.register(Post)
admin.site.register(People)
admin.site.register(Comment)
admin.site.register(Like)