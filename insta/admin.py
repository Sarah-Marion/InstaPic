from django.contrib import admin
from .models import Profile, Image, Comment, Like, Follow

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)