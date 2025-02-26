# relationship_app/query_samples.py
from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # 1. Query all books by a specific author
        author_name = "J.K. Rowling"
        books_by_author = Book.objects.filter(author__name=author_name)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(book.title)

        # 2. List all books in a library
        library_name = "Central Library"
        try:
            library = Library.objects.get(name=library_name)
            books_in_library = library.books.all()
            print(f"\nBooks in {library_name}:")
            for book in books_in_library:
                print(book.title)
        except Library.DoesNotExist:
            print(f"No library found with name {library_name}")

        # 3. Retrieve the librarian for a library
        librarian = Librarian.objects.filter(library__name=library_name).first()
        if librarian:
            print(f"\nLibrarian of {library_name}: {librarian.name}")
        else:
            print(f"No librarian found for {library_name}")
