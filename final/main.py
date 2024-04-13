from project import login
from project import add_item
from project import view_cart
from project import search_item
from project import update_quantity
from project import remove_item
from project import checkout

while True:
        print("Welcome to the Shopping Cart:")                         # Welcome to the Shopping Cart:
        print("1. Login")                                              # 1. Login
        print("2. Add items to the cart")                              # 2. Add items to the cart
        print("3. View cart")                                          # 3. View cart
        print("4. Search for a item in the cart")                      # 4. Search for a item in the cart
        print("5. Update product quantity in the cart")                # 5. Update product quantity in the cart
        print("6. Remove a product from the cart")                     # 6. Remove a product from the cart
        print("7. Checkout")                                           # 7. Checkout
        print("8. Exit")                                               # 8. Exit

        choice = int(input("Enter your choice: "))                     # Enter your choice: 1

        if choice == 1:
            if login():
                                                                            # If login is successful and returns true
                while True:
                    print("Select what you want to do: ")                   # Select what you want to do:
                    print("1. Add a product to the cart")                   # 1. Add a product to the cart
                    print("2. View cart")                                   # 2. View cart
                    print("3. Search for a product in the cart")            # 3. Search for a product in the cart
                    print("4. Update product quantity in the cart")         # 4. Update product quantity in the cart
                    print("5. Remove a product from the cart")              # 5. Remove a product from the cart
                    print("6. Checkout")                                    # 6. Checkout
                    print("7. Logout")                                      # 7. Logout
                    
                    inner_choice = int(input("Enter your choice: "))        # 7
                    
                    if inner_choice == 7:
                        print("Thank you for using the shopping cart!")     # Thank you for using the shopping cart!
                        print("Logging out...")                             # Logging out...
                        break                                               # Logout
                    elif inner_choice == 1:
                        add_item()
                    elif inner_choice == 2:
                        view_cart()
                    elif inner_choice == 3:
                        search_item()
                    elif inner_choice == 4:
                        update_quantity()
                    elif inner_choice == 5:
                        remove_item()
                    elif inner_choice == 6:
                        checkout()
                    else:
                        print("Invalid choice. Please try again.\n")
            else:
                continue  # Retry login if unsuccessful
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Please login first.")