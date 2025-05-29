from django.db import models

from core.models import BaseModel

# Create your models here.
class Post(BaseModel):
    title = models.CharField(
        max_length=32,
    )
    body = models.TextField()
    likes = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return f"{self.id}) {self.title}"


class Comment(BaseModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.TextField()
    likes = models.PositiveIntegerField(
        default=0,
    )
