from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=255)

class FavoriteUserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    add_date = models.DateTimeField(default=timezone.now)