from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.CharField(max_length=150, primary_key=True, unique=True, verbose_name="사용자 아이디")
    password = models.CharField(max_length=20, blank=False, verbose_name="비밀번호")
    nickname = models.CharField(max_length=20, null=True, blank=False, verbose_name="닉네임")
    
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
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="사용자")
    nickname = models.CharField(max_length=20, null=True, blank=False, verbose_name="닉네임")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = self.user_id.nickname  # 해당 사용자의 닉네임으로 채움
        super().save(*args, **kwargs)


class Comment(models.Model):
    comment_number = models.AutoField(default=0, primary_key=True)
    post_number = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)