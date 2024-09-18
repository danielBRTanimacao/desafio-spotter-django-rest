from django.urls import path
from .views import BookApiView, BookDetailApiView, AuthorApiView, AuthorDetailApiView

urlpatterns = [
    path('books/', BookApiView.as_view(), name='books'),
    path('books/<int:id>/', BookDetailApiView.as_view(), name='specific_book'),
    path('authors/', AuthorApiView.as_view(), name='authors'),
    path('authors/<int:id>/', AuthorDetailApiView.as_view(), name='specific_author'),
    # path('register/', CreationApiView.as_view(), name='register'),
    # path('login/', LoginApiView.as_view(), name='login'),
    # path('user/', UserApiView.as_view(), name='user'),
]
