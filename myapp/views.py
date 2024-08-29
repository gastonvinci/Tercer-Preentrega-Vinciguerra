from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, PublisherForm
from .models import Author, Book, Publisher

# Vista para inicio
def home(request):
    return render(request, 'myapp/home.html')

# Vista para manejar el formulario de Author
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')  # Redirige a la lista de autores
    else:
        form = AuthorForm()
    return render(request, 'myapp/add_author.html', {'form': form})

# Vista para manejar el formulario de Book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirige a la lista de libros después de guardar
    else:
        form = BookForm()
    return render(request, 'myapp/add_book.html', {'form': form})

# Vista para manejar el formulario de Publisher
def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')  # Redirige a la lista de editores
    else:
        form = PublisherForm()
    return render(request, 'myapp/add_publisher.html', {'form': form})

# Vista para listar autores
def author_list(request):
    authors = Author.objects.all()  # Obtiene todos los autores
    return render(request, 'myapp/author_list.html', {'authors': authors})

# Vista para listar libros
def book_list(request):
    books = Book.objects.all()  # Obtiene todos los libros
    return render(request, 'myapp/book_list.html', {'books': books})

# Vista para listar editores
def publisher_list(request):
    publishers = Publisher.objects.all()  # Obtiene todos los editores
    return render(request, 'myapp/publisher_list.html', {'publishers': publishers})
