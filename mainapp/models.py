from django.db import models


class Post(models.Model):
    content = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return f"id: {self.id}"
