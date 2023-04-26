from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

CATEGORY = (
    ("music", "music"),
    ("education", "education"),
    ("technology", "technology"),
)

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=200, choices=CATEGORY)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
