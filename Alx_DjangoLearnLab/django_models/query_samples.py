import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

for author in Author.objects.all():
    print(author.name)

for book in Book.objects.all():
    print(f"{book.title} - by {book.author.name}")

for library in Library.objects.all():
    print(library.name)

for librarian in Librarian.objects.all():
    print(f"{librarian.name} - works at {librarian.library.name}")
