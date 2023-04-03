from django.contrib import admin

from .models import Book, BookInstance, Genre, Author, Language

# Register your models here.

# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

class BookInline(admin.TabularInline):
    model = Book
    extra = 0

# define the Author admin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    
    fields = ['first_name', 'last_name', ('date_of_birth' , 'date_of_death')]
    
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)
 

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")

    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','display_book','borrower', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldset = (
        (None, {
            'field': ('book', 'imprint', 'id')
            
            }),
        ('Availability', {
            'field': ('status', 'due_back', 'borrower')
            }),

        )

