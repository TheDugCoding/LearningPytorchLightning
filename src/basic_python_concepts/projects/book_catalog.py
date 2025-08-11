from utilities import retrieve_data_path
import json
from typing import NamedTuple

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

class BookAttributes(NamedTuple):
    title: str
    author: str
    genre: str
    publication_year: str

class Catalog:
    def __init__(self):
        self.books = []

    #this solution is not scalable, everytime we add a new attributes for a book we also need to add in multiple lines of code
    def add_book(self, title, author, genre, publication_year):
        if None in (title, author, genre, publication_year):

            try:
                if title and author and genre and publication_year:
                    self.books.append(create_book(title, author, genre, publication_year))
                    #print(f'Book {title} {author} {genre} {publication_year} successfully added.')
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

    def add_book_from_user(self):
        title = input('what is the title?\n')
        author = input('who is the author?\n')
        genre = input('what is the genre?\n')
        publication_year = input('what is the publication_year?\n')
        self.books.append(create_book(title, author, genre, publication_year))
        # print(f'Book {title} {author} {genre} {publication_year} successfully added.')

    def retrieve_books(self):
        return self.books

    def find_books_by_author(self, author):
        books_by_author = []
        for book in self.books:
            if book['author'] == author:
                books_by_author.append(book)

        return books_by_author

    def find_books_by_genre(self, genre):
        books_by_genre = []
        for book in self.books:
            if book['genre'] == genre:
                books_by_genre.append(book)

        return books_by_genre

    def shows_books(self, books):
        for book in books:
            print(book['title'], book['author'], book['genre'], book['publication_year'])

    def save_catalog(self):
        with open(retrieve_data_path().joinpath('basic_python_data/projects/book_catalog/catalog.json'), "w") as f:
            json.dump([book for book in self.books], f, indent=4)

    def load_catalog(self):
        with open(retrieve_data_path().joinpath('basic_python_data/projects/book_catalog/catalog.json'), "r") as f:
            data = json.load(f)
        return data


def create_book(title, author, genre, publication_year):

        book = {
            'title': title,
            'author': author,
            'genre': genre,
            'publication_year': publication_year
        }

        return book

if __name__ == '__main__':

    new_catalog = Catalog()

    new_catalog.add_book("The Last Dawn", "Ava Harper", "Science Fiction", "2020")
    new_catalog.add_book("Echoes of Silence", "Liam Gray", "Mystery", "2019")
    new_catalog.add_book("Whispers in the Wind", "Ava Harper", "Romance", "2021")
    new_catalog.add_book("Crimson Sky", "Ethan Black", "Fantasy", "2018")
    new_catalog.add_book("The Forgotten Code", "Zara Lane", "Thriller", "2020")
    new_catalog.add_book("Beneath the Ice", "Liam Gray", "Mystery", "2022")
    new_catalog.add_book("Celestial Bound", "Ava Harper", "Science Fiction", "2023")
    new_catalog.add_book("The Obsidian Path", "Ethan Black", "Fantasy", "2021")
    new_catalog.add_book("Flicker", "Nina Storm", "Young Adult", "2020")
    new_catalog.add_book("Chasing Fire", "Zara Lane", "Thriller", "2021")

    new_catalog.add_book("Midnight's Edge", "Cole Bennett", "Horror", "2017")
    new_catalog.add_book("Iron Veil", "Zara Lane", "Thriller", "2019")
    new_catalog.add_book("The Willow Tree", "Maya James", "Drama", "2020")
    new_catalog.add_book("Parallel", "Ava Harper", "Science Fiction", "2024")
    new_catalog.add_book("Vanishing Point", "Liam Gray", "Mystery", "2020")
    new_catalog.add_book("Wanderlust", "Nina Storm", "Young Adult", "2019")
    new_catalog.add_book("Kingdom of Ash", "Ethan Black", "Fantasy", "2020")
    new_catalog.add_book("Broken Compass", "Cole Bennett", "Horror", "2021")
    new_catalog.add_book("The Mind Trap", "Zara Lane", "Thriller", "2023")
    new_catalog.add_book("Night Pulse", "Liam Gray", "Mystery", "2024")

    new_catalog.add_book("Fragments", "Ava Harper", "Romance", "2019")
    new_catalog.add_book("Shadowlight", "Ethan Black", "Fantasy", "2022")
    new_catalog.add_book("Among the Stars", "Ava Harper", "Science Fiction", "2021")
    new_catalog.add_book("The Reckoning", "Cole Bennett", "Horror", "2020")
    new_catalog.add_book("Twilight Games", "Nina Storm", "Young Adult", "2021")
    new_catalog.add_book("Code Phantom", "Zara Lane", "Thriller", "2022")
    new_catalog.add_book("Deep Waters", "Maya James", "Drama", "2021")
    new_catalog.add_book("Dead End Street", "Liam Gray", "Mystery", "2023")
    new_catalog.add_book("Into the Ember", "Ethan Black", "Fantasy", "2019")
    new_catalog.add_book("Fading Colors", "Maya James", "Drama", "2022")

    new_catalog.add_book("Dark Echo", "Zara Lane", "Thriller", "2018")
    new_catalog.add_book("Gravity Lost", "Ava Harper", "Science Fiction", "2019")
    new_catalog.add_book("The Pale Mirror", "Cole Bennett", "Horror", "2018")
    new_catalog.add_book("Spellbound", "Ethan Black", "Fantasy", "2023")
    new_catalog.add_book("Starcrossed", "Nina Storm", "Young Adult", "2022")
    new_catalog.add_book("Fractured Hour", "Zara Lane", "Thriller", "2024")
    new_catalog.add_book("Curtain Call", "Maya James", "Drama", "2023")
    new_catalog.add_book("Final Clue", "Liam Gray", "Mystery", "2025")
    new_catalog.add_book("Neon Rain", "Ava Harper", "Science Fiction", "2025")
    new_catalog.add_book("Blood Pact", "Ethan Black", "Fantasy", "2024")

    new_catalog.add_book("Afterglow", "Maya James", "Drama", "2024")
    new_catalog.add_book("The Hollow", "Cole Bennett", "Horror", "2022")
    new_catalog.add_book("Rewind", "Nina Storm", "Young Adult", "2023")
    new_catalog.add_book("Oblivion Run", "Zara Lane", "Thriller", "2025")
    new_catalog.add_book("Lightbearer", "Ethan Black", "Fantasy", "2025")
    new_catalog.add_book("Starborn", "Ava Harper", "Science Fiction", "2022")
    new_catalog.add_book("Haunted Dreams", "Cole Bennett", "Horror", "2023")
    new_catalog.add_book("Secrets of the Sea", "Maya James", "Drama", "2025")
    new_catalog.add_book("The Maze", "Liam Gray", "Mystery", "2021")
    new_catalog.add_book("Awakening", "Nina Storm", "Young Adult", "2024")

    #testing
    books_in_catalog = new_catalog.retrieve_books()
    new_catalog.shows_books(books_in_catalog)
    new_catalog.save_catalog()
    new_catalog.shows_books(new_catalog.load_catalog())
    new_catalog.add_book_from_user()

