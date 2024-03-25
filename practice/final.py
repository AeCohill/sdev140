class Book:
    def __init__(self, title, author, publisher):
        self._title = title
        self._author = author
        self._publisher = publisher

    # Accessor methods
    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_publisher(self):
        return self._publisher

    # Mutator methods
    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author

    def set_publisher(self, publisher):
        self._publisher = publisher

    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, Publisher: {self._publisher}"
