# Parent Class
class Book:
    def __init__(self, title, author, pages):
        self.title = title               # Public attribute
        self.author = author             # Public attribute
        self._pages = pages              # Protected attribute

    # Method to display book info
    def info(self):
        return f"'{self.title}' by {self.author}, {self._pages} pages."

    # Method to update pages (encapsulation example)
    def update_pages(self, new_pages):
        if new_pages > 0:
            self._pages = new_pages
        else:
            print("Page count must be positive!")

# Child Class (Inheritance)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)  # Initialize parent attributes
        self.__file_size = file_size            # Private attribute

    # Override the info method (polymorphism example)
    def info(self):
        return f"'{self.title}' by {self.author}, {self._pages} pages, File size: {self.__file_size}MB."

    # Method to update file size (encapsulation example)
    def update_file_size(self, new_size):
        if new_size > 0:
            self.__file_size = new_size
        else:
            print("File size must be positive!")

# Create an object of the Book class
physical_book = Book("The Hair Library", "A. Promise UAntioje", 58)
print(physical_book.info())  # Output: 'The Hair Library' by A. Promise Uantioje, 58 pages.

# Create an object of the EBook class
ebook = EBook("1958", "Chinue Achebe", 209, 2.5)
print(ebook.info())  # Output: '1958' by Chinue Achebe, 209 pages, File size: 2.5MB.

# Update attributes using methods
physical_book.update_pages(120)
print(physical_book.info())  # Output: 'The Hair Library' by A. Promise Uantioje, 58 pages.

ebook.update_file_size(3.0)
print(ebook.info())  # Output: '1958' by Chinue Achebe, 209 pages, File size: 3.0MB