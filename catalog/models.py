import uuid
from datetime import date
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):

    name = models.CharField(
        max_length=200, help_text="Enter book genre (e.g Science Fiction)"
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    """Model represent a book but not a specific copy"""

    title = models.CharField(max_length=200)

    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)

    summery = models.TextField(
        max_length=1000, help_text="Enter a brief description about the book"
    )

    isbn = models.CharField(
        "ISBN",
        max_length=13,
        help_text='ISBN 13 character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
    )

    genre = models.ManyToManyField(Genre, help_text="Select genre for this book")

    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True)

    def __str__(self):

        return self.title

    def get_absolute_url(self):
        """Return the URL to access the detail record for this book"""
        return reverse("book-detail", args=[str(self.id)])

    def display_genre(self):
        """ create a string representing the first three genre if any"""
        return ", ".join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = "Genre"

class BookInstance(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text="unique id represent each copy"
    )

    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)

    imprint = models.CharField(max_length=200)

    due_back = models.DateField(null=True, blank=True)

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintanace"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )
    status = models.CharField(
        max_length=1,
        default="m",
        choices=LOAN_STATUS,
        blank=True,
        help_text="book availability",
    )

    class Meta:
        ordering = ["due_back"]
        permissions = (("can mark as returned", "set book as returned"),)


    def __str__(self):
        return f"{self.id} ,({self.book.title})"


    def display_book(self):
        return self.book.title


    def is_overdue(self):
        return bool(self.due_back and date.today() > self.due_back)

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_absolute_url(self):

        return reverse("author-detail", args=[str(self.id)])


class Language(models.Model):

    name = models.CharField(
        max_length=200,
        help_text="write natural langauge for a book (e.g English, Frech, Germany etc",
    )

    def __str__(self):

        return self.name
