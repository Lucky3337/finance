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
    # files = models.ManyToManyRel()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Document(models.Model):
    """Class about documents(for examples: .docx, .doc, .xlsx etc.)"""

    name = models.CharField(verbose_name="Наименование файла", max_length=350)
    date_created = models.DateTimeField(verbose_name="Дата загрузки файла")
    user = models.OneToOneField(User, verbose_name="Пользователь/Автор", on_delete=models.CASCADE, null=False)
    post_id = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE, null=False)
    document = models.FileField(upload_to='upload_documents')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.name


class Image(models.Model):
    """Class about images"""

    name = models.CharField(verbose_name="Наименование изображения", max_length=350)
    date_created = models.DateTimeField(verbose_name="Дата загрузки изображения")
    user = models.OneToOneField(User, verbose_name="Пользователь/Автор", on_delete=models.CASCADE, null=False)
    post_id = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE, null=False)
    photo = models.ImageField(upload_to='upload_images')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.name


class Index:
    """Class about filling main site page (right menu, content, news)"""

    """This method forms list categories consist of posts """
    @classmethod
    def get_categories(cls):
        categories = Category.objects.all()
        right_menu = {}
        for category in categories:
            posts = Post.objects.filter(category_id=category.id)
            list_dict_posts = []
            for post in posts:
                list_dict_posts.append([str(post.id), str(post.title)])
            right_menu[str(category.name)] = list_dict_posts
        return right_menu
