from django.db import models
from django.contrib.auth.models import User
from collections import defaultdict


class Category(models.Model):
    """Class of menu of category"""

    name = models.CharField(verbose_name="Название", max_length=350)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Post(models.Model):
    """Class about blog post"""

    title = models.CharField(verbose_name="Заголовок", max_length=350)
    text = models.TextField(verbose_name="Содержание")
    date_created = models.DateTimeField(verbose_name="Дата создания")
    category_id = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, verbose_name='Пользователь/Автор', on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Index:
    """Class about filling main site page (right menu, content, news)"""

    """This method forms list categories consist of posts """
    @classmethod
    def get_categories(cls):
        categories = Category.objects.all()
        right_menu = defaultdict(list)
        for category in categories:
            posts = Post.objects.filter(category_id=category.id)
            for post in posts:
                right_menu[str(category.name)].append(post.title)
        right_menu = sorted(right_menu.items())
        return right_menu
