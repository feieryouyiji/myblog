from django.db import models

# Create your models here.

from django.db import models


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name


class Tag(models.Model):
    name = models.CharField(max_length=64)  # tag

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64)  # 类别

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=64)  # 文章标题
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    summary = models.CharField(max_length=64)  # 文章摘要
    content = models.TextField()  # 文章内容

    is_publish = models.BooleanField(default=True)  # 是否发布

    author = models.CharField(max_length=64)  # 文章作者
    created_time = models.DateTimeField(auto_now_add=True)  # 创建时间 修改之后不会更新
    modify_time = models.DateTimeField(auto_now=True)  # 修改之后自动与当前时间一致

    def __str__(self):
        return str(self.pk)

# 测试一对一
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
