from django.contrib import admin
from .models import Post

# basic custom admin interface for our Post model
class post_admin(admin.ModelAdmin):
    search_fields = ["id", "content"]
    list_display = ("id", "content")


admin.site.register(Post, post_admin)
