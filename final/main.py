class Library:
    def __init__(self, listofBooks):
        # Initialize the Library object with a list of books
        self.books = listofBooks

    def displayAvailableBooks(self):
        # Display the number and names of available books in the library
        print(f"\n{len(self.books)} AVAILABLE BOOKS ARE: ")
        for book in self.books:
            print(" -- " + book)
        print("\n")

    def borrowBook(self, name, bookname):
        # Borrow a book from the library
        if bookname not in self.books:
            print(f"{bookname} BOOK NOT AVAILABLE !\n")
        else:
            # Add borrower's name and book name to the tracking list
            track.append({name: bookname})
            print("BOOK ISSUED SUCCESSFULLY.\n")
            # Remove the borrowed book from the library
            self.books.remove(bookname)

    def returnBook(self, bookname):
        # Return a borrowed book to the library
        print("BOOK RETURNED : THANK YOU! \n")
        # Add the returned book back to the library
        self.books.append(bookname)

    def donateBook(self, bookname):
        # Donate a book to the library
        print("BOOK DONATED\n")
        # Add the donated book to the library
        self.books.append(bookname)


class Student():
    def requestBook(self):
        # Prompt the student to request a book for borrowing
        print("Which book would you like to borrow?")
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        # Prompt the student to return a borrowed book
        print("Please fill in your details to proceed")
        name = input("Enter your name: ")
        self.book = input("Enter the name of the book you want to return: ")
        if {name: self.book} in track:
            # Remove the returned book from the tracking list
            track.remove({name: self.book})
        return self.book

    def donateBook(self):
        # Prompt the student to donate a book to the library
        print("Thank you for choosing to donate!")
        self.book = input("Enter the name of the book you want to donate: ")
        return self.book


if __name__ == "__main__":

    # Initialize the library with initial list of books
    UPESlibrary = Library(
        ["Spiderlight", "Neverwhere", "Berserk", "Ellen", "Circe", "Frankeistein"])
    # Create an instance of Student class
    student = Student()
    # Initialize the tracking list for borrowed books
    track = []

    # Display welcome message and options menu
    print("\t\t\t\t\t\t\t WELCOME TO THE UPES LIBRARY \n")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. List all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. Exit the library\n""")

    # Continuously prompt the user for input until they choose to exit
    while (True):
        try:
            usr_response = int(input("Enter your choice: "))

            # Perform actions based on user's choice
            if usr_response == 1:  
                UPESlibrary.displayAvailableBooks()
            elif usr_response == 2: 
                UPESlibrary.borrowBook(
                    input("Enter your name: "), student.requestBook())
            elif usr_response == 3:
                UPESlibrary.returnBook(student.returnBook())
            elif usr_response == 4:
                UPESlibrary.donateBook(student.donateBook())
            elif usr_response == 5:
                # Display all currently borrowed books and borrowers
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                # Display a message if no books are currently borrowed
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
            
            elif usr_response == 6:
                # Exit the program
                print("THANK YOU! \n")
                exit()
            else:
                print("INVALID INPUT! \n")
        except Exception as e:
            # Handle exceptions for invalid inputs
            print(f"{e}---> INVALID INPUT! \n")
