class Book:
    def __init__(self, book_id, content):
        self.id = book_id
        self.content = content
        self.font_size = 12
        # self.screen_size = self.calculate_screen(self.font_size)


class Section:
    def __init__(self, section_name):
        self.section_name = section_name
        self.books = []
        self.capacity = 50

    def add_book(self, book):
        if len(self.books) < self.capacity:
            self.books.append(book)
            return "Book Added"

        return "Capacity Reached"


class Library:
    def __init__(self, name):
        self.name = name
        self.section_count = 8
        self.sections = {}
