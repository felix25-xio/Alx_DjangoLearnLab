from bookshelf.models import Book

Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)

from bookshelf.models import Book Book.objects.all() <QuerySet [<Book: Book object (1)>]>

from bookshelf.models import Book title = "Nineteen Eighty-Four" new_book.save()

from bookshelf.models import Book

new_book.delete() (1, {'bookshelf.Book': 1}) Book.objects.all() <QuerySet []>

