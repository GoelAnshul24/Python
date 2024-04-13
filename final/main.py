import pandas as pd

class Library:
    def __init__(self, listofBooks):
        # Initialize the Library object with a list of books
        self.books_df = pd.DataFrame({"book_name": listofBooks, "borrowed_by": [""]*len(listofBooks)})
        self.track_df = pd.DataFrame(columns=["borrower", "book_name"])

    def displayAvailableBooks(self):
        # Display the number and names of available books in the library
        print(f"\n{len(self.books_df)} AVAILABLE BOOKS ARE: ")
        print(self.books_df.to_string(index=False))
        print("\n")

    def borrowBook(self, name, bookname):
        # Borrow a book from the library
        if bookname not in self.books_df['book_name'].values:
            print(f"{bookname} BOOK NOT AVAILABLE !\n")
        elif self.books_df.loc[self.books_df['book_name'] == bookname, 'borrowed_by'].iloc[0] != "":
            print(f"{bookname} BOOK IS ALREADY BORROWED !\n")
        else:
            # Add borrower's name to the book DataFrame
            self.books_df.loc[self.books_df['book_name'] == bookname, 'borrowed_by'] = name
            # Add borrower's name and book name to the tracking DataFrame
            self.track_df = self.track_df.append({"borrower": name, "book_name": bookname}, ignore_index=True)
            print("BOOK ISSUED SUCCESSFULLY.\n")

    def returnBook(self, bookname):
        # Return a borrowed book to the library
        if bookname not in self.books_df['book_name'].values:
            print(f"{bookname} BOOK DOES NOT BELONG TO THE LIBRARY !\n")
        elif self.books_df.loc[self.books_df['book_name'] == bookname, 'borrowed_by'].iloc[0] == "":
            print(f"{bookname} BOOK IS NOT BORROWED !\n")
        else:
            # Remove borrower's name from the book DataFrame
            self.books_df.loc[self.books_df['book_name'] == bookname, 'borrowed_by'] = ""
            # Remove the returned book from the tracking DataFrame
            self.track_df = self.track_df[self.track_df['book_name'] != bookname]
            print("BOOK RETURNED : THANK YOU! \n")

    def donateBook(self, bookname):
        # Donate a book to the library
        self.books_df = self.books_df.append({"book_name": bookname, "borrowed_by": ""}, ignore_index=True)
        print("BOOK DONATED\n")

    def trackBooks(self):
        # Display all currently borrowed books and borrowers
        if len(self.track_df) > 0:
            print("BOOKS CURRENTLY BORROWED:")
            print(self.track_df.to_string(index=False))
            print("\n")
        else:
            print("NO BOOKS ARE ISSUED!. \n")


class Student:
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

    # Display welcome message and options menu
    print("\t\t\t\t\t\t\t WELCOME TO THE UPES LIBRARY \n")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. List all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. Exit the library\n""")

    # Continuously prompt the user for input until they choose to exit
    while True:
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
                UPESlibrary.trackBooks()
            elif usr_response == 6:
                # Exit the program
                print("THANK YOU! \n")
                break
            else:
                print("INVALID INPUT! \n")
        except ValueError:
            # Handle exceptions for invalid inputs
            print("INVALID INPUT! \n")
