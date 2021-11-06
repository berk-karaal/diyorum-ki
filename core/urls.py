from django.contrib import admin
from django.urls import path
from mainapp.views import home, best_posts, like, new_post
import os

urlpatterns = [
    path(f"{os.environ.get('ADMIN_PAGE_URL')}/", admin.site.urls),
    path("", home, name="home"),
    path("en_begenilen/", best_posts, name="best_posts"),
    path("like/<int:id>", like, name="like"),
    path("yeni/", new_post, name="new_post"),
]
