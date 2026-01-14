import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

print("\nAUTHORS")
for a in Author.objects.all():
    print(a.name)

print("\nBOOKS")
for b in Book.objects.all():
    print(b.title, "->", b.author.name)

print("\nLIBRARIES")
for l in Library.objects.all():
    print(l.name, ":", l.books.count(), "books")

print("\nLIBRARIANS")
for lb in Librarian.objects.all():
    print(lb.name, "works at", lb.library.name)

