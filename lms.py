class Library():
    def __init__(self):
        try:
            self.file = open("lib.txt", "a+")
        except FileNotFoundError:
            print("the file cannot be opened")
        self.menu()

    def menu(self):
        deger = input("1) List Books \n 2) Add Book\n 3) Remove Book\n 4) Quit\n Enter the operation you want to perform:")
        if deger == "1":
            self.listBooks()
        elif deger == "2":
            self.addBook()
        elif deger == "3":
            self.removeBook()
        elif deger.lower() == "q":
            print("have a nice day")
            self.__del__()
        else:
            print("Enter the valid value.")
            self.menu()
            





    def __del__(self):
        self.file.close()
    def listBooks(self):
        self.file.seek(0)
        content = self.file.read()
        if not content:
            print("No books found.")
        else:
            books_info = content.splitlines()
            for book_info in books_info:
                book_details = book_info.split(',')
                book_name = book_details[0]
                author = book_details[1]
                print(f"Book Name: {book_name}, Author: {author}")
        self.menu()
    def addBook(self):
        book_title = input("Enter the title of the book: ")
        book_author = input("Enter the author of the book: ")
        year = input("Enter the release year: ")
        number_of_page = input("Enter the number of pages: ")
        book_info = f"{book_title},{book_author},{year},{number_of_page}\n"
        self.file.write(book_info)
        print("Book added successfully.")
        self.menu()
    def removeBook(self):
        self.file.seek(0)
        content = self.file.read()

        if len(content) == 0 or content == ' ':
            print("there is not any book. Please try again.")
        else:
            book_to_remove = input("Enter the title of the book to remove: ")
            self.file.seek(0)
            books_info = self.file.read().splitlines()
            updated_books_info = [book for book in books_info if not book.startswith(book_to_remove + ',')]
            self.file.truncate(0)
            for i in updated_books_info:
                self.file.write(i + "\n")
            print(f"Book '{book_to_remove}' removed successfully.")
        self.menu()
lib = Library()