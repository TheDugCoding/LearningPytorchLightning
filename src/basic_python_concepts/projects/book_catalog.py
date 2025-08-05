'''
You are tasked with building a command-line Book Catalog Manager that allows users to manage a personal
collection of books. Each book should have a title, author, genre, and publication year.
The program must allow users to add new books, view all books in the catalog, search for books by author
or genre, load book data from a JSON file, and save the catalog back to a file. To complete this exercise, you must
use core Python concepts including classes (for the Book and Catalog), dictionaries (to represent book data),
tuples (for returning multiple values from functions), lists (to store the catalog), loops (for iterating through books),
and list comprehensions (for filtering results). You should also include user input handling, conditional logic with if/else statements,
file reading/writing with error handling using exceptions, and organize your code using functions.
This project is designed to give you hands-on experience with the foundational tools introduced in Python Crash Course.


'''

class Catalog:
    def __init__(self):
        self.books = []

    #this solution is not scalable, everytime we add a new attributes for a book we also need to add in multiple lines of code
    def add_book(self, title, author, genre, publication_year):
        try:
            if title and author and genre and publication_year:
                self.books.append(Book(title, author, genre, publication_year))
            else:
                s = ''
                if not title:
                    s += ' title'
                if not author:
                    s += ' author'
                if not genre:
                    s += ' genre'
                if not publication_year:
                    s += ' publication_year'
                raise ValueError('Missing fields:' + str(s))
        except ValueError as err:
            print(err)

    def retrieve_books(self):
        return self.books

    def find_books_by_author(self, author):
        books_by_author = []
        for book in self.books:
            if book.author == author:
                books_by_author.append(book)

        return books_by_author

    def find_books_by_genre(self, genre):
        books_by_genre = []
        for book in self.books:
            if book.genre == genre:
                books_by_genre.append(book)

        return books_by_genre


class Book:
    def __init__(self, title, author, genre, publication_year):

        self.book = {
            'title': title,
            'author': author,
            'genre': genre,
            'publication_year': publication_year
        }

    def get_book(self):
        return self.book

if __name__ == '__main__':

    new_catalog = Catalog()
    new_catalog.add_book('', '', '', '2020')