from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'author: {self.author.first_name} book name: {self.name}'

class FavoriteUserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    add_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.user.username}'


@receiver(post_save, sender=User)
def add_favorite_user_book(sender, instance, created, **kwargs):
    if created:
        FavoriteUserBook.objects.create(user=instance)