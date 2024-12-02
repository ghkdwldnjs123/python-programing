class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.price == other.price
        return False
    
book1 = Book("Python Programming", "김대열", 999.99)
book2 = Book("Artificial adventure", "대열킴", 999.99)

book1.display_info()
book2.display_info()
    
print(book1 == book2)