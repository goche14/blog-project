from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300)
    avatar = models.ImageField()

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=50)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.text

class Tag(models.Model):
    posts = models.ManyToManyField(Post)
    name = models.TextField(max_length=200)
    
    def __str__(self):
        return self.name