import pandas as pd
from django.http import HttpResponse
from .models import Book

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book


from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookUpdateForm

def update_book(request, book_id):
    # Get the book to update
    book = get_object_or_404(Book, pk=book_id)

    # If the form is submitted with POST data, update the book
    if request.method == 'POST':
        form = BookUpdateForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Save the updated data
            return redirect('home')  # Redirect to the home page or book list page
    else:
        form = BookUpdateForm(instance=book)

    return render(request, 'update_book.html', {'form': form, 'book': book})

def import_csv(request):
    # Load CSV file into DataFrame (Assume it's in the same directory as manage.py)
    df = pd.read_csv('readyfordatabase.csv')

    # Iterate through rows and save data to the database
    for index, row in df.iterrows():
        book = Book(
            chindi=row['chindi'],
            cenglish=row['cenglish'],
        )
        book.save()

    return HttpResponse("CSV data imported successfully!")


from django.shortcuts import render
def home(request):
    # Get all books from the database
    books = Book.objects.all()

    # Set the number of items per page
    paginator = Paginator(books, 5)  # Show 5 books per page

    # Get the current page number
    page_number = request.GET.get('page')

    # Get the books for the current page
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html',{'page_obj': page_obj})

