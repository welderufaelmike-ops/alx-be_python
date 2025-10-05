
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f'"{self.title}" by {self.author}'


class Library:
    def __init__(self):
        self._books = []  # Private list of Book objects

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f'Checked out: {book}'
        return f'Book "{title}" is not available.'

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f'Returned: {book}'
        return f'Book "{title}" was not checked out.'

    def list_available_books(self):
        available = [str(book) for book in self._books if book.is_available()]
        return available if available else ["No books available."]

         
    
