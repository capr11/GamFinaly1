from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    title = models.CharField(
        max_length=123
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    file = models.ImageField(
        upload_to='media/games_detail_images'
    )
    def clean(self):
        # Проверка типа файла (например, только изображения)
        if not self.file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            raise ValidationError('File must be a PNG, JPG, or JPEG image')


class Game(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=123
    )
    description = models.TextField()
    logo = models.ImageField(
        upload_to='media/games_logo'
    )
    images = models.ManyToManyField(
        Image
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        auto_now=True
    )

    def clean(self):
        # Валидация для Game
        if not self.title:
            raise ValidationError('Title cannot be empty')
        if self.description and len(self.description) < 10:
            raise ValidationError('Description must be at least 10 characters long')

    def __str__(self):
        return self.title


