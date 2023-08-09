from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=256)
    nickname = models.CharField(max_length=30, unique=True, null=True, blank=False, verbose_name="닉네임")
    
    def save(self, *args, **kwargs):
        is_new = False
        if not self.pk:
            is_new = True

        super().save(*args, **kwargs)

        if is_new:
            post = Post(user=self, nickname=self.nickname)
            post.save()

class Post(models.Model):
    post_number = models.AutoField(default=0, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, null=True, default="default_nickname")
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment_number = models.AutoField(default=0, primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)