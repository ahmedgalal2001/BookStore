from django.shortcuts import render,redirect , get_object_or_404
from .models import Book

books = [
    {
        "book_id": 1,
        "title": "Book Title",
        "author": "Book Author",
        "publisher": "Book Publisher",
        "publication_date": "2020-01-01",
        "image": "https://cdn.pixabay.com/photo/2015/11/19/21/10/glasses-1052010_640.jpg",
        "price": 19.99,
        "genre": "Fiction",
        "rating": 4.5,
        "views": 100,
        "description": "A brief description of the book."
    },
]


def bookstore(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, "base/bookstore.html" , context=context)






def bookstoreAdd(request):
    if request.method == 'POST':
        try:
            book = Book.objects.create(
                title=request.POST.get('title'),
                author=request.POST.get('author'),
                publisher=request.POST.get('publisher'),
                publication_date=request.POST.get('publication_date'),
                image=request.POST.get('image'),
                price=request.POST.get('price'),
                genre=request.POST.get('genre'),
                description=request.POST.get('description')
                )
            book.save()
            return redirect('/')
        except ValueError as e:
            print(f"Data conversion error: {e}")
            return render(request, 'base/bookstoreadd.html', {'error': 'Invalid data format. Please check your inputs.'})
    return render(request, 'base/bookstoreadd.html')


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