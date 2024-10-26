from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    create_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
