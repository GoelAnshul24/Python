# Dictionary named "users" which is used to store credentials of the user
users = {"Harshit": "500125668"}      # we can add more users as per our choice

# Class named "Item" to represent items in the shopping cart
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
# Class named "ShoppingCart" to represent the shopping cart functionality
class ShoppingCart:
    def __init__(self):
        # Empty list to store items in the shopping cart
        self.items = []
        
    # Function of Adding an item to the shopping cart
    def add_item(self, item, quantity):
        self.items.append({"item": item, "quantity": quantity})
    
    # To Remove items
    def remove_item(self, index):
        del self.items[index]

    # To Update Quantity of item
    def update_quantity(self, index, new_quantity):
        self.items[index]["quantity"] = new_quantity

    # To view items in cart
    def view_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Items in your shopping cart:")
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. {item['item'].name} - {item['item'].price} INR - Quantity: {item['quantity']}")
    # Checkout
    def checkout(self):
        total_price = sum(item['item'].price * item['quantity'] for item in self.items)
        print("Items in your shopping cart:")
        for item in self.items:
            print(f"{item['item'].name} - Price: {item['item'].price} INR - Quantity: {item['quantity']}")
        print(f"Total Price: {total_price} INR")

# Class named "ShoppingSystem" to manage the overall shopping system
class ShoppingSystem:
    def __init__(self):
        # Creating a new 'ShoppingCart' object to handle shopping cart functionality
        self.shopping_cart = ShoppingCart()

    # User Login
    def login(self):
        username = input("Enter Username: ")       # Harshit
        password = input("Enter Password: ")       # 500125668
        # Check if the entered username exists in the 'users dictionary' and if the password is correct or not...
        if username in users and users[username] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def add_item_to_cart(self, item, quantity):
        # Pass the item and quantity to the 'add_item' function of the "ShoppingCart" object
        self.shopping_cart.add_item(item, quantity)

    def remove_item_from_cart(self, index):
        # Pass the index to the 'remove_item' function of the "ShoppingCart" object
        self.shopping_cart.remove_item(index)

    def update_item_quantity(self, index, new_quantity):
        # Pass the index and new quantity to the 'update_quantity' function of the "ShoppingCart" object
        self.shopping_cart.update_quantity(index, new_quantity)

    def view_cart(self):
        # Call 'the view_cart' function of the "ShoppingCart" object
        self.shopping_cart.view_cart()

    def checkout(self):
        # Call the 'checkout' function of the "ShoppingCart" object
        self.shopping_cart.checkout()


# Creating an object of the 'ShoppingSystem' class to start the shopping system
system = ShoppingSystem()

# Defining some items
items = [Item("Smartphone", 7000), Item("Laptop", 14000), Item("Basketball", 20000), Item("Shoes", 2000)]

# Main loop of the shopping cart
while True:
    
    print("Welcome to the Shopping Cart:")                      # Welcome to the Shopping Cart:
    if system.login():  # Calling 'Login' Fucntion
        
        while True:
            print("Select what you want to do: ")               # Select what you want to do:
            print("1. Add a product to the cart")               # 1. Add a product to the cart
            print("2. View cart")                               # 2. View cart
            print("3. Update product quantity in the cart")     # 3. Update product quantity in the cart
            print("4. Remove a product from the cart")          # 4. Remove a product from the cart
            print("5. Checkout")                                # 5. Checkout
            print("6. Logout")                                  # 6. Logout
            
            choice = int(input("Enter your Choice: "))          # Enter your Choice: 
            if choice == 1:
                print("Available Items:")
                for index, item in enumerate(items, start=1):
                    print(f"{index}. {item.name} - Price: {item.price} INR")
                item_index = int(input("Enter the index of the item you want to add: "))  # Enter the index of the item you want to add:
                quantity = int(input("Enter the quantity: "))                             # Enter the quantity:
                system.add_item_to_cart(items[item_index - 1], quantity)
            elif choice == 2:
                system.view_cart()
            elif choice == 3:
                system.view_cart()
                index = int(input("Enter the index of the item you want to update: "))    # Enter the index of the item you want to update:
                new_quantity = int(input("Enter the new quantity: "))                     # Enter the new quantity:
                system.update_item_quantity(index - 1, new_quantity)
            elif choice == 4:
                system.view_cart()
                index = int(input("Enter the index of the item you want to remove: "))    #Enter the index of the item you want to remove:
                system.remove_item_from_cart(index - 1)
            elif choice == 5:
                system.checkout()
            elif choice == 6:
                print("Thank you for using the shopping cart!")                           # Thank you for using the shopping cart!
                print("Logging Out...")                                                   # Logging Out...
                break
            else:
                print("Invalid choice. Please try again.")                                # Invalid choice. Please try again.
    else:
        print("Please login first.")   # If login is unsuccessful, it prints "Please login first."