
from django.db import models

class CatPost(models.Model):
    STATUS_CHOICES = [
        ("Lost", "Lost"),
        ("Found", "Found"),
    ]

    image = models.ImageField(upload_to='cat_images/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(CatPost, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"
