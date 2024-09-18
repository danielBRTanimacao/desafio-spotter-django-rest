from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book, FavoriteUserBook
from .serializers import AuthorSerializer, BookSerializer, FavoriteUserBookSerializer

class BookApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        # modificando aqui
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class BookDetailApiView(APIView):
    def get(self, request, id):
        book = get_object_or_404(Book, pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, id):
        book = get_object_or_404(Book, pk=id)
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        # modificando aqui ainda falta fazer um validador
        book = get_object_or_404(Book, pk=id)
        book_name = book.name
        book.delete()
        return Response({'message': f'Book deleted "{book_name}"'}, status=status.HTTP_204_NO_CONTENT)
    
class AuthorApiView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        ...
    
class AuthorDetailApiView(APIView):
    def get(self, request, id):
        author = get_object_or_404(Book, pk=id)
        serializer = BookSerializer(author)
        return Response(serializer.data)