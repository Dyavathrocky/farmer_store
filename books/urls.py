from django.urls import path
from .views import BookListView , BookDetailView , SearchResultListView

urlpatterns = [
    path("", BookListView.as_view(),name="book_list"),
    #path("<int:pk>/" , BookDetailView.as_view(), name="book_deatil"),
    path("<uuid:pk>/" , BookDetailView.as_view(), name="book_deatil"),
    path("search/", SearchResultListView.as_view(), name="search"),
]
