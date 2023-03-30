from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(blank=True, unique=True)
#     github_id = models.CharField(max_length=100, blank=True, null=True)

#---------------Post---------------------

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('なし', 'なし'),
        ('AI', 'AI'),
        ('Python', 'Python'),
        ('java', 'java'),
    )

    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='post_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='post_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='post_images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='post_images/', null=True, blank=True)
    # image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='なし')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "投稿"
        verbose_name_plural = "投稿一覧"


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')
        verbose_name = 'ポストいいね'
        verbose_name_plural = 'ポストいいね一覧'

class PostRead(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#---------------Talk---------------------

class Talk(models.Model):
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='talk_likes', blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name = "トーク"
        verbose_name_plural = "トーク一覧"

class TalkLike(models.Model):
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('talk', 'user')
        verbose_name = 'トークいいね'
        verbose_name_plural = 'トークいいね一覧'

class TalkRead(models.Model):
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 