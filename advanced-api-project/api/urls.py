from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BoookDeleteView


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', BoookDeleteView.as_view(), name='book-delete'),
]