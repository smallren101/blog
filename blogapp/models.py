from django.contrib.auth.models import AbstractUser
from django.db import models

# 创建种类表
class Category(models.Model):
    id = models.AutoField(primary_key=True)    # 主键
    name = models.CharField(max_length=24)     # 种类名
    def __str__(self):
        return self.name

# 用户表
class User_info(AbstractUser):                      # 继承
    useremail = models.EmailField()                  # 注册邮箱
    userurl = models.URLField()                      # 注册url
    def __str__(self):
        return self.username

# 创建评论表
class Comment(models.Model):
    content = models.CharField(max_length=1024)                          # 评论内容
    isarticle = models.CharField(max_length=512)                           # 被评论的文章
    date_publish = models.DateTimeField(auto_now=True)                   # 评论时间
    user_info = models.ForeignKey(User_info, on_delete=models.CASCADE)   # 评论用户的信息
    def __str__(self):
        return self.content

# 创建文章表
class Article(models.Model):
    id = models.AutoField(primary_key=True)                                        # 主键
    name = models.CharField(max_length=64)                                         # 文章名
    content = models.TextField()                                                   # 文章内容
    describe = models.CharField(max_length=50, default=None)                       # 文章概述
    date_publish = models.DateTimeField(auto_now=True)                             # 创建时间
    click_count = models.IntegerField()                                            # 浏览
    author = models.ForeignKey(User_info, on_delete=models.CASCADE)                # 作者
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)         # 评论
    tag = models.ForeignKey(Category, on_delete=models.CASCADE)                    # 一个种类可对应多篇文章
    def __str__(self):
        return self.name