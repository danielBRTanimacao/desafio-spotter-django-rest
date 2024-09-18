from django.contrib import admin
from api.models import Author, Book, FavoriteUserBook

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
    )
    ordering = '-id',
    search_fields = (
        'id',
        'first_name',
        'last_name',
    )
    list_per_page = 10
    list_max_show_all = 150
    list_display_links = 'id', 'first_name',

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = 'id', 'author', 'name',
    ordering = '-id',
    search_fields = (
        'id',
        'author',
        'name',
    )
    list_per_page = 10
    list_max_show_all = 150
    list_display_links = 'id', 'author',

@admin.register(FavoriteUserBook)
class FavoriteUserBookAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'book',
    ordering = '-id',
    search_fields = (
        'id',
        'user',
        'book',
    )
    list_per_page = 10
    list_max_show_all = 150
    list_display_links = 'id', 'user',