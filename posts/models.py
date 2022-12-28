from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=200, default='Adeyinka' )
    title = models.CharField(max_length=200, default= 'First Post')
    text = models.TextField()

    def __str__(self):
        return self.title