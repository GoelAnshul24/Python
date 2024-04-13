import pandas as pd

class Library:
    def __init__(self, listofBooks):
        self.books_df = pd.DataFrame({"book_name": listofBooks, "borrowed_by": [""]*len(listofBooks)})
        self.track_df = pd.DataFrame(columns=["borrower", "book_name"])

    def displayAvailableBooks(self):
        print(f"\n{len(self.books_df)} AVAILABLE BOOKS ARE: ")
        print(self.books_df.to_string(index=False))
        print("\n")

    def borrowBook(self, name, bookname):
        if bookname not in self.books_df['book_name'].values:
            print(f"{bookname} BOOK NOT AVAILABLE !\n")
        elif self.books_df.loc[self.books_df['book_name'] == bookname, 'borrowed_by'].iloc[0] != "":
            print(f"{bookname} BOOK IS ALREADY BORROWED !\n")
        else:
            self.books_df.loc[self.books_df['book_name'] == bookname, 'borrowed_by'] = name
            self.track_df = self.track_df.append({"borrower": name, "book_name": bookname}, ignore_index=True)
            print("BOOK ISSUED SUCCESSFULLY.\n")

    def returnBook(self, bookname):
        if bookname not in self.books_df['book_name'].values:
            print(f"{bookname} BOOK DOES NOT BELONG TO THE LIBRARY !\n")
        elif self.books_df.loc[self.books_df['book_name'] == bookname, 'borrowed_by'].iloc[0] == "":
            print(f"{bookname} BOOK IS NOT BORROWED !\n")
        else:
            self.books_df.loc[self.books_df['book_name'] == bookname, 'borrowed_by'] = ""
            self.track_df = self.track_df[self.track_df['book_name'] != bookname]
            print("BOOK RETURNED : THANK YOU! \n")

    def donateBook(self, bookname):
        self.books_df = self.books_df.append({"book_name": bookname, "borrowed_by": ""}, ignore_index=True)
        print("BOOK DONATED\n")

    def trackBooks(self):
        if len(self.track_df) > 0:
            print("BOOKS CURRENTLY BORROWED:")
            print(self.track_df.to_string(index=False))
            print("\n")
        else:
            print("NO BOOKS ARE ISSUED!. \n")


class Student:
    def requestBook(self):
        print("Which book would you like to borrow?")
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        print("Please fill in your details to proceed")
        name = input("Enter your name: ")
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

    def donateBook(self):
        print("Thank you for choosing to donate!")
        self.book = input("Enter the name of the book you want to donate: ")
        return self.book


    UPESlibrary = Library(
        ["Spiderlight", "Neverwhere", "Berserk", "Ellen", "Circe", "Frankeistein"])
    student = Student()
    print("\t\t\t\t\t\t\t WELCOME TO THE UPES LIBRARY \n")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. List all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. Exit the library\n""")
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
