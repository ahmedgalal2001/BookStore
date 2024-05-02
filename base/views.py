from django.shortcuts import render,redirect


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
        "description": "A brief description of the book."
    },
    {
        "book_id": 2,
        "title": "Another Book",
        "author": "Another Author",
        "publisher": "Another Publisher",
        "publication_date": "2021-01-01",
        "image": "https://cdn.pixabay.com/photo/2015/11/19/21/10/glasses-1052010_640.jpg",
        "price": 29.99,
        "genre": "Non-Fiction",
        "description": "A brief description of another book."
    },
    {
        "book_id": 3,
        "title": "Third Book",
        "author": "Third Author",
        "publisher": "Third Publisher",
        "publication_date": "2022-01-01",
        "image": "https://cdn.pixabay.com/photo/2015/11/19/21/10/glasses-1052010_640.jpg",
        "price": 39.99,
        "genre": "Fiction",
        "description": "A brief description of the third book."
    },
    {
        "book_id": 4,
        "title": "Fourth Book",
        "author": "Fourth Author",
        "publisher": "Fourth Publisher",
        "publication_date": "2023-01-01",
        "image": "https://cdn.pixabay.com/photo/2015/11/19/21/10/glasses-1052010_640.jpg",
        "price": 49.99,
        "genre": "Non-Fiction",
        "description": "A brief description of the fourth book."
    },
    {
        "book_id": 5,
        "title": "Fifth Book",
        "author": "Fifth Author",
        "publisher": "Fifth Publisher",
        "publication_date": "2024-01-01",
        "image": "https://cdn.pixabay.com/photo/2015/11/19/21/10/glasses-1052010_640.jpg",
        "price": 59.99,
        "genre": "Fiction",
        "description": "A brief description of the fifth book."
    },
    {
        "book_id": 6,
        "title": "Sixth Book",
        "author": "Sixth Author",
        "publisher": "Sixth Publisher",
        "publication_date": "2025-01-01",
        "image": "https://cdn.pixabay.com/photo/2015/11/19/21/10/glasses-1052010_640.jpg",
        "price": 69.99,
        "genre": "Non-Fiction",
        "description": "A brief description of the sixth book."
    },
]


def bookstore(request):
    context = {'books': books}
    return render(request, "base/bookstore.html" , context=context)






def bookstoreAdd(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            author = request.POST.get('author')
            publisher = request.POST.get('publisher')
            publication_date = request.POST.get('publication_date')
            image = request.POST.get('image')
            
            # Convert price to float, handle ValueError
            price = float(request.POST.get('price'))
            
            genre = request.POST.get('genre')
            description = request.POST.get('description')

            # Append the book data to the list with a new ID
            books.append({
                "book_id": len(books) + 1,
                "title": title,
                "author": author,
                "publisher": publisher,
                "publication_date": publication_date,
                "image": image,
                "price": price,
                "genre": genre,
                "description": description
            })
            return redirect('/')
        except ValueError as e:
            print(f"Data conversion error: {e}")
            return render(request, 'base/bookstoreadd.html', {'error': 'Invalid data format. Please check your inputs.'})
    return render(request, 'base/bookstoreadd.html')


def bookstoreShow(request, book_id):
    context = None;
    for book in books:
        if book['book_id'] == int(book_id):
            context = {'book': book}
    return render(request, "base/bookstoreshow.html" , context=context)

def bookstoreEdit(request, book_id):
    context = None;
    for book in books:
        if book['book_id'] == int(book_id):
            context = {'book': book}
            if request.method == 'POST':
                try:
                    book['title'] = request.POST.get('title')
                    book['author'] = request.POST.get('author')
                    book['publisher'] = request.POST.get('publisher')
                    book['publication_date'] = request.POST.get('publication_date')
                    book['image'] = request.POST.get('image')
                    book['price'] = float(request.POST.get('price'))
                    book['genre'] = request.POST.get('genre')
                    book['description'] = request.POST.get('description')
                    return redirect('/')
                except ValueError as e:
                    print(f"Data conversion error: {e}")
                    return render(request, 'base/bookstoreadd.html', {'error': 'Invalid data format. Please check your inputs.'})
    return render(request, "base/bookstoreedit.html" , context=context)

def bookstoreDelete(request, book_id):
    context = None;
    for book in books:
        if book['book_id'] == int(book_id):
            books.remove(book)
    return redirect('/')