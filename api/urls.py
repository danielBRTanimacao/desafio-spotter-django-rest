from django.urls import path
from api import views

urlpatterns = [
    path('books/', views.BookApiView.as_view(), name='books'),
    path('books/<int:id>/', views.BookDetailApiView.as_view(), name='specific_book'),
    path('authors/', views.AuthorApiView.as_view(), name='authors'),
    path('authors/<int:id>/', views.AuthorDetailApiView.as_view(), name='specific_author'),
    path('register/', views.UserRegisterApiView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('user/', views.UserApiView.as_view(), name='user'),
]
