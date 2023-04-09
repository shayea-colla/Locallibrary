from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),

    path("books/", views.BookListView.as_view(), name="book"),
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),
    path("book/<uuid:pk>/renew/", views.renew_book_librarian, name="renew_book_librarian"),
    path("mybook/", views.LoanedBooksBuyUserListView.as_view(), name="my-borrowed"),

    path("authors/", views.author_list, name="author"),
    path("authors/<int:pk>",views.author_detail, name="author-detail"),

    #Tmp path for testing porpuse
    path('tmp/', views.tmp, name="tmp"),
]
