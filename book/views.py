from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from django.views.decorators.http import require_POST
from .models import Book
from django.db.models import Q

@login_required(login_url='user:login')
def AddBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book:book_list')
    
    else:
        form = BookForm()

    return render(request, 'book/add_book.html', {'form':form})


def BookList(request):
    query = request.GET.get('search')
    books = Book.objects.all()

    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    context = {'books': books, 'search_query': query}
    return render(request, 'book/book_list.html', context)
