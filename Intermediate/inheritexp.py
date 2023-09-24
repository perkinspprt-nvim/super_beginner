
class Book:
    def __init__(self, title, pages):
        self.title = title;
        self.pages = int(pages);

    def describe(self):
        print(f"\n{self.title} has been read.");
        print(f"What a great book, it has {self.pages} pages");
        return 0;

class Novel(Book):
    def __init__(self, title, pages, isFiction):
        super().__init__(title, pages);
        self.isFiction = bool(isFiction);
    
    def describe(self):
        print(f"\n{self.title} has been read");
        print(f"What a great book, it has {self.pages} pages");
        if self.isFiction == True:    
            print(f"{self.title} is a work of fiction.");
        elif self.isFiction == False:
            print(f"{self.title} is not a work of fiction.");


Book_1 = Novel("Thrilling Tales of dragons", 200, True);
Book_2 = Book("Atomic Habits", 300);
shelf  = [Book_1, Book_2];

for book in shelf:
    book.describe();

 
