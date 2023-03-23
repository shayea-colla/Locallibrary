from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre, Language
# Create your views here.


def index(request):

    num_books = Book.objects.count()

    num_instances = BookInstance.objects.count()

    num_instance_available = BookInstance.objects.filter(status='a').count()

    num_authors = Author.objects.count()
    
    genre_types = Genre.objects.all()

    book_sampls = Book.objects.all()[:5]

    num_visit = request.session.get('num_visit', 0)
    request.session['num_visit'] = num_visit + 1;

    context = {
            'book_sampls': book_sampls,
            'num_books':num_books,
            'num_instances': num_instances,
            'num_instance_available': num_instance_available,
            'num_authors': num_authors,
            'genre_types': genre_types,
            }
    return render(request, 'catalog/index.html', context=context)


def author_list(request):
    """ get all authors from db"""
    
    authors = Author.objects.all()
    
    return render(request, 'catalog/author_list.html', {
        'authors': authors,
        })

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    books = Book.objects.filter(author=author.id)
    number_of_book =  Book.objects.filter(author=author.id).count()

    return render(request, 'catalog/author_detail.html', {
        'author': author,
        'books': books,
        'number_of_book': number_of_book,
        })



#class AuthorDetailView(generic.DetailView):
#    model = Author
#    self.object          


class BookListView(generic.ListView):
    model = Book
    context_type = "book_list"
    queryset = Book.objects.all()



class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 3 


