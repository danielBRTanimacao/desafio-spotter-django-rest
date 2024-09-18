from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Author, Book, FavoriteUserBook
from .serializers import AuthorSerializer, BookSerializer, FavoriteUserBookSerializer, UserSerializer

class BookApiView(APIView):
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return super().get_permissions()

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

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
        return Response(serializer.data)
    
    def put(self, request, id):
        book = get_object_or_404(Book, pk=id)
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
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
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    

class AuthorDetailApiView(APIView):
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'DELETE' or self.request.method == 'PUT':
            return [IsAuthenticated()]
        return super().get_permissions()

    def get(self, request, id):
        author = get_object_or_404(Book, pk=id)
        serializer = BookSerializer(author)
        return Response(serializer.data)

    def put(self, request, id):
        author = get_object_or_404(Author, pk=id)
        serializer = BookSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        author = get_object_or_404(Author, pk=id)
        author_name = author.name
        author.delete()
        return Response({'message': f'Author deleted "{author_name}"'}, status=status.HTTP_204_NO_CONTENT)
    

class UserRegisterApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "All fields are need"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "User exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create(username=username, password=password)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserLoginApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid fields"}, status=status.HTTP_400_BAD_REQUEST)


class UserApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # add book

    # remove book