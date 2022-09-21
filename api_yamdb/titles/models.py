from django.db import models


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=200)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Категория', max_length=200)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField('Название', max_length=255)
    year = models.DateField('Год')
    category = models.ForeignKey(
        'Категория',
        Category,
        on_delete=models.PROTECT,
        related_name='titles'
    )
    genre = models.ForeignKey(
        'Жанр',
        Genre,
        on_delete=models.PROTECT,
        related_name='titles'
    )

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
