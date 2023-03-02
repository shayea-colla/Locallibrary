from django.contrib import admin

from .models import Book, BookInstance, Genre, Author, Language

#Register your models here.
#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Genre)
#admin.site.register(Author)
admin.site.register(Language)

# define the Author admin
class AuthorAdmin(models.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(models.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(modles.ModelAdmin):
    pass
