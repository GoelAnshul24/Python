import datetime
import List_of_books


class Book:                                  # This class is used to keep records of all books.
    def __init__(self, title, author):       #__init__ is used as a constructor and initialize the newly created object(self)
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}
        self.users = {"admin": "password"}

    def add_book(self, book):                                                     #Add books
        self.books.append(book)                                                   #f is a function helps to write all details of braces
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def remove_book(self, title):                                                 #Remove books
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                if book.title in self.borrowed_books:
                    del self.borrowed_books[book.title]
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def display_books(self):                                                       #Display books
        if self.books:
            print("Books available in the library:")
            for index, book in enumerate(self.books, 1):
                print(f"{index}. '{book.title}' by {book.author}")
        else:
            print("No books available in the library.")

    def search_book(self, query):                                                  #search for a book
        found_books = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                found_books.append(book)
        if found_books:
            print(f"Found {len(found_books)} book(s) matching '{query}':")
            for index, book in enumerate(found_books, 1):                         #enumerate is used for containing a count from start, which defaults to zero.
                print(f"{index}. '{book.title}' by {book.author}")
        else:
            print(f"No books found matching '{query}'.")

    def borrow_book(self, title, user):                                          #for borrowing books
        if title in self.borrowed_books:
            print("This book is already borrowed.")
            return
        for book in self.books:
            if book.title == title:
                due_date = datetime.date.today() + datetime.timedelta(days=14) 
                self.borrowed_books[title] = {"borrower": user, "due_date": due_date}
                print(f"Book '{title}' borrowed by {user}. Due date: {due_date}.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title, user):                                         #for returning books
        if title not in self.borrowed_books:
            print("This book is not borrowed.")
            return
        if self.borrowed_books[title]["borrower"] != user:
            print("You are not the borrower of this book.")
            return
        del self.borrowed_books[title]
        print(f"Book '{title}' returned by {user}.")

    def authenticate_user(self, username, password):                            #verification of the user
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False

def main():
    library = Library()
    logged_in_user = None

    while True:
        print("\nLibrary Management System")
        print("1. Log in")                                
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Display available books")
        print("5. Search for a book")
        print("6. Borrow a book")
        print("7. Return a book")
        print("8. Display borrowed books")
        print("9. Log out")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            if logged_in_user:
                print("You are already logged in.")
            else:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if library.authenticate_user(username, password):
                    logged_in_user = username
                    print("Login successful.")
                else:
                    print("Invalid username or password.")
        elif choice == '2':
            if logged_in_user:
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                new_book = Book(title, author)
                library.add_book(new_book)
            else:
                print("You need to log in to add a book.")
        elif choice == '3':
            if logged_in_user:
                title = input("Enter the title of the book to remove: ")
                library.remove_book(title)
            else:
                print("You need to log in to remove a book.")
        elif choice == '4':
            for i in range(5):
                print(List_of_books.Books[i],"\t",List_of_books.Author[i])
        elif choice == '5':
            query = input("Enter title or author to search: ")
            library.search_book(query)
        elif choice == '6':
            if logged_in_user:
                title = input("Enter the title of the book to borrow: ")
                library.borrow_book(title, logged_in_user)
            else:
                print("You need to log in to borrow a book.")
        elif choice == '7':
            if logged_in_user:
                title = input("Enter the title of the book to return: ")
                library.return_book(title, logged_in_user)
            else:
                print("You need to log in to return a book.")
        elif choice == '8':
            if logged_in_user:
                for key, value in library.borrowed_books.items():
                    print(f"book: {key}, info: {value}")
            else:
                print("You need to log in to see your borrowed books.")
        elif choice == '9':
            logged_in_user = None
            print("Logged out.")
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()