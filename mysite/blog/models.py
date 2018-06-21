from django.db import models

# Create your models here.

class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)#博客标题
    body = models.TextField()#博客正文
    timestamp = models.DateTimeField()#创建时间



