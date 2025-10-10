
class Book:
    def __init__(self,title:int, author: str):
        self.title=title
        self.author=author

    def info(self):
        return f"{self.title} by {self.author}"
    def __str__(self):
        return f" Book: {self.info()} "
    

class EBook(Book):
    def __init__(self, title, author, file_size:int ):
        super().__init__(title, author)            
        self.file_size=file_size


    def __str__(self):
        return f"EBook: {self.info()} file size {self.file_size}KB"
        return super().__str__()    
    
class PrintBook(Book):
    def __init__(self, title, author, page_count:int):
        super().__init__(title, author)    

    def __str__(self):
        return f"PrintBook:  {self.info()} page count self.page_count"
        return super().__str__()

class Library:
    def __init__(self):
        self.books = []  # This is composition: Library HAS books
    
    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library is empty.")
            return
        for book in self.books:
            print(book)