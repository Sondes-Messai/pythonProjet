
from django.shortcuts import render
from Library.catalog.models import Author
from models import Book, State
def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_book_reserved =State.object.filter(status="r").count()
    return render(request, 'catalog/books.html',
                  context={
                      'num_books': num_books,
                      'num_author': num_authors,       
                      
                  },
