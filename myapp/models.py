from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Add this line
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title