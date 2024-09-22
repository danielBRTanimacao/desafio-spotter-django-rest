from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Author, Book, FavoriteUserBook
from .serializers import AuthorSerializer, BookSerializer, UserSerializer, FavoriteUserBookSerializer

class BookApiView(APIView):
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return super().get_permissions()

    def get(self, request):
        books = Book.objects.all()

        search_query = request.query_params.get('search', None)
        if search_query:
            books = books.filter(name__icontains=search_query)

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetailApiView(APIView):
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'DELETE' or self.request.method == 'PUT':
            return [IsAuthenticated()]
        return super().get_permissions()

    def get(self, request, id):
        book = get_object_or_404(Book, pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        book = get_object_or_404(Book, pk=id)
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, id):
        book = get_object_or_404(Book, pk=id)
        book_name = book.name
        book.delete()
        return Response({'message': f'Book deleted "{book_name}"'}, status=status.HTTP_204_NO_CONTENT)


class AuthorApiView(APIView):
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return super().get_permissions()
    
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AuthorDetailApiView(APIView):
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'DELETE' or self.request.method == 'PUT':
            return [IsAuthenticated()]
        return super().get_permissions()

    def get(self, request, id):
        author = get_object_or_404(Author, pk=id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        author = get_object_or_404(Author, pk=id)
        serializer = BookSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, id):
        author = get_object_or_404(Author, pk=id)
        author_name = author.name
        author.delete()
        return Response({'message': f'Author deleted "{author_name}"'}, status=status.HTTP_204_NO_CONTENT)


class UserRegisterApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        authenticate(serializer)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserLoginApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(serializer, User)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = FavoriteUserBook.objects.all().filter(user=request.user.id)
        serializer = FavoriteUserBookSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        number_of_books = FavoriteUserBook.objects.count()
        if number_of_books > 20:
            return Response({"message": "limit 20 books"}, status=status.HTTP_100_CONTINUE)
        book = FavoriteUserBookSerializer(data=request.data)
        book.is_valid(raise_exception=True)
        book.save()
        return Response(book.data, status=status.HTTP_201_CREATED)


class UserDetailApiView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        favorite_book = get_object_or_404(FavoriteUserBook, pk=id)
        serializer = FavoriteUserBookSerializer(favorite_book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        favorite_book = get_object_or_404(FavoriteUserBook, pk=id)
        favorite_book = favorite_book.book.name
        favorite_book.delete()
        return Response(favorite_book.data, status=status.HTTP_201_CREATED)