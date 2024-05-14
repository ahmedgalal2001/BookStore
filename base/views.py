from django.shortcuts import render,redirect , get_object_or_404
from django.contrib.auth import logout, authenticate, login
from .models import Book
from django.contrib.auth.models import User
from .forms import BookForm
def bookstore(request):
    books = Book.objects.all().filter(user=request.user)
    context = {'books': books}
    return render(request, "base/bookstore.html" , context=context)


def bookstoreAdd(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Get the currently logged-in user
            user = request.user
            # Create a new book instance from the form data
            new_book = form.save(commit=False)
            # Set the user field of the book to the currently logged-in user
            new_book.user = user
            # Save the book instance
            new_book.save()
            return redirect('bookstore')  # Redirect to bookstore or any other page
    else:
        form = BookForm()
    return render(request, 'base/bookstoreadd.html', {'form': form})

def bookstoreShow(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, "base/bookstoreshow.html" , context=context)

def bookstoreEdit(request, book_id):
    context = None
    book  = None
    try:
        if request.method == 'GET':
            book = get_object_or_404(Book, pk=int(book_id))
        if request.method == 'POST':
            book = get_object_or_404(Book, pk=int(request.POST.get('id')))
            book.title = request.POST.get('title')
            book.author = request.POST.get('author')
            book.publisher = request.POST.get('publisher')
            book.publication_date = request.POST.get('publication_date')
            book.image = request.POST.get('image')
            book.price = request.POST.get('price')
            book.genre = request.POST.get('genre')
            book.description = request.POST.get('description')
            book.save()
            return redirect('/')
        context = {'book': book}
    except ValueError as e:
        print(f"Data conversion error: {e}")
        return render(request, 'base/bookstoreadd.html', {'error': 'Invalid data format. Please check your inputs.'})
    return render(request, "base/bookstoreedit.html" , context=context)

def bookstoreDelete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('/')

from django.contrib.auth import authenticate, login

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_page = request.GET.get('next', 'bookstore')
            return redirect(next_page)
        else:
            # Authentication failed
            return render(request, 'base/userlogin.html', {'error': 'Invalid username or password.'})
    return render(request, 'base/userlogin.html')


def userlogout(request):
    print("userlogout")
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return redirect('/')
def userregister(request):
    try:
        if request.method == 'POST':
            user = User.objects.create(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
                is_superuser=False,
                email=request.POST.get('email'),
                first_name=request.POST.get('fname'),
                last_name=request.POST.get('lname')
            )
            user.save()
            return redirect('/user/login')
    except ValueError as e:
        print(f"Data conversion error: {e}")
        return render(request, 'base/userregisterion.html', {'error': 'Invalid data format. Please check your inputs.'})
    return render(request, 'base/userregisterion.html')