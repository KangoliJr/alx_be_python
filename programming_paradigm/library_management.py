class Book:
    
    def __init__(self, title, author):
        self.title = title       # Public attribute
        self.author = author     # Public attribute
        self._is_checked_out = False  # Private attribute

    def __str__(self):
        return f"{self.title} by {self.author}"

    def is_available(self):
        return not self._is_checked_out

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return
        self._books.append(book)
        print(f"'{book.title}' by {book.author} has been added to the library.") 

    def check_out_book(self, title):
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.is_available():
                    book.checked_out()
                    print(f"'{title}' has been successfully checked out.") 
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        if not found:
            print(f"Book with title '{title}' not found in the library.") 
            pass 

    def return_book(self, title):
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if not book.is_available(): 
                    book.returned_book()
                    print(f"'{title}' has been successfully returned.") 
                    return
                else:
                    print(f"'{title}' was not checked out (already available).") 
                    return
        if not found:
            print(f"Book with title '{title}' not found in the library.") 
            pass 

    def list_available_books(self):
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book)
                available_count += 1
        
        if available_count == 0 and len(self._books) > 0:
            print("No books are currently available.")
        elif len(self._books) == 0:
            print("The library is empty.")