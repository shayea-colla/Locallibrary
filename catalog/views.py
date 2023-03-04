from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre, Language
# Create your views here.


def index(request):

    num_books = Book.objects.count()

    num_instances = BookInstance.objects.count()

    num_instance_available = BookInstance.objects.filter(status='a').count()

    num_authors = Author.objects.count()
    
    genre_types = Genre.objects.all()

    book_sampls = Book.objects.all()[:5]
    context = {
            'book_sampls': book_sampls,
            'num_books':num_books,
            'num_instances': num_instances,
            'num_instance_available': num_instance_available,
            'num_authors': num_authors,
            'genre_types': genre_types,
            }
    return render(request, 'catalog/index.html', context=context)
