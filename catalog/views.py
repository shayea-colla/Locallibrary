from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .forms import RenewBookForm
from .models import Book, Author, BookInstance, Genre, Language

# Create your views here.
def index(request):
    num_books = Book.objects.count()

    num_instances = BookInstance.objects.count()

    num_instance_available = BookInstance.objects.filter(status="a").count()

    num_authors = Author.objects.count()

    genre_types = Genre.objects.all()

    book_sampls = Book.objects.all()[:5]

    num_visit = request.session.get("num_visit", 0)
    request.session["num_visit"] = num_visit + 1

    context = {
        "book_sampls": book_sampls,
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instance_available": num_instance_available,
        "num_authors": num_authors,
        "genre_types": genre_types,
    }
    return render(request, "catalog/index.html", context=context)


def author_list(request):
    """get all authors from db"""

    authors = Author.objects.all()

    return render(
        request,
        "catalog/author_list.html",
        {
            "authors": authors,
        },
    )


def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    books = Book.objects.filter(author=author.id)
    number_of_book = Book.objects.filter(author=author.id).count()

    return render(
        request,
        "catalog/author_detail.html",
        {
            "author": author,
            "books": books,
            "number_of_book": number_of_book,
        },
    )


def tmp(request):
    return render(request, "catalog/tmp.html")


# class AuthorDetailView(generic.DetailView):
#    model = Author
#    self.object


class BookListView(generic.ListView):
    model = Book
    context_type = "book_list"
    queryset = Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 3


class LoanedBooksBuyUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = "catalog/bookinstance_list_borrowed_user.html"
    paginate_by = 10

    def get_querySet(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact="o")
            .order_by(due_back)
        )

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == "POST":
        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required 
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
        else:
            context = {
                'form': form,
                'book_instance': book_instance,
            }

            return render(
                request,
                "catalog/book_renew_librarian.html",
                {
                    "context": context,
                })


        # Redirect to the new URL:
        return HttpResponseRedirect(reverse('my-borrowed'))

    else:
        proposed_renewal_data = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_data': proposed_renewal_data})

        context = {
            'form': form,
            'book_instance': book_instance,
        }
        return render(
            request,
            "catalog/book_renew_librarian.html",
            {
                "context": context,
            })
        
