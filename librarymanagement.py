class Book:
    def __init__(self,isbn,title,author):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checkedOut = False
        self.reserved = False
    
    def checkout(self):
        if self.checkedout:
            return False
        self.checkedOut = True
        return True

    def reserve(self):
        if self.reserved:
            return False
        self.reserved = True
        return True
    
    def unreserve(self):
        self.reserved = False
        return True
    
    def return_book(self):
        self.checkedOut = False
        return True
    
class User:
    def __init__(self,userId):
        self.userId = userId
        self.checkedout_books = []
        self.reserved_books = []

    def checkout_book(self,book: Book):
        if not book.checkout():
            print(f"Book {book.isbn} cannot be checked out since it's already checked out.")
            return
        self.checkedout_books.append(book)

    def reserve_book(self,book: Book):
        if not book.reserve():
            print(f"Book {book.isbn} cannot be reserved since it's already reserved.")
            return
        self.reserved_books.append(book)
    
    def return_book(self,book: Book):
        if book not in self.checkedout_books:
            print(f"This book hasn't been checked out by {self.userId}")
        book.return_book
        self.checkedout_books.remove(book)

class Library:
    def __init__(self):
        books = {}

    def add_book(self,book: Book):
        self.books[book.isbn] = book

    def remove_book(self,book: Book):
        del self.books[book.isbn]
    
    def find_book(self,isbn):
        if self.books[isbn]:
            return self.book[isbn]
        print(f"Couldn't find the book with the isbn {isbn}")

    def show_all_books(self):
        for book in self.books.values():
            print(f"Book - {book.title} Checkedout - {book.checkedOut} Reserved - {book.reserved}")

        