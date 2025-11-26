from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(default='def_post.png', blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    date_published = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title