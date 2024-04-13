# Dictionary named "users" which is used to store credentials of the user
users = {
    "Harshit": "500125668",
    "xyz": "abc123",
    # we can add more users as per our choice
}


# Empty shopping cart as a list of dictionaries
shopping_cart = []

# Function to log in to the cart
def login():
    
    '''Returns--> True if login is successful, Otherwise False.'''
    
    username = input("Enter Username: ")       #xyz
    password = input("Enter Password: ")       #abc123
    if username in users and users[username] == password:
        print("Login successful!")             #Login successful!
        return True
    else:
        print("Invalid username or password.")
        return False


# Function to add an item to the cart
def add_item():
    dict = {
        1: {"name": "Smartphone", "price": 17000},
        2: {"name": "Laptop", "price": 41000},
        3: {"name": "Headphones", "price": 5000},
        4: {"name": "Shoes", "price": 7500},
        5: {"name": "Pen", "price": 90},
        6: {"name": "Basketball", "price": 1000},
        7: {"name": "Chips", "price": 50},
        8: {"name": "Book", "price": 200},
        9: {"name": "Bottle", "price": 100},
        10: {"name": "Bag", "price": 2000}
    }
    for key, value in dict.items():
        print(f"{key}. {value['name']} - {value['price']} INR")
    item_no = int(input("Enter the serial number of the item: "))  #1
    if item_no in dict:
        item_quantity = int(input("Enter the quantity of the item: "))  #1
        item = {
            "name": dict[item_no]["name"],    #Smartphone
            "price": dict[item_no]["price"],  #17000
            "quantity": item_quantity         #1
        }
        shopping_cart.append(item)            
        print(f"{dict[item_no]['name']} added to the cart.\n")  # Smartphone added to the cart
    else:
        print("Invalid item number. Please try again.")


# Function to view items in the cart
def view_cart():
    if not shopping_cart:
        print("Your shopping cart is empty.\n")
    else:
        print("Items in your shopping cart:")
        for index, item in enumerate(shopping_cart, start=1):
            print(f"{index}. {item['name']} - {item['price']} INR - Quantity: {item['quantity']}")    # 1. Smartphone - 17000 INR - Quantity: 1
        print()   #prints new line
        
        
# Function to search an item in the cart
def search_item():
    if not shopping_cart:
        print("Your shopping cart is empty.\n")
        return
    
    search = input("Enter the name of the item you want to search for: ")    # smart
    found_items = []
    
    # Search for items in the cart matching the search query
    for item in shopping_cart:
        if search.lower() in item['name'].lower():
            found_items.append(item)
    
    if found_items:
        print(f"Found {len(found_items)} item(s) matching '{search}':")      #Found 1 item(s) matching 'smart': 
        for index, found_item in enumerate(found_items, start=1):
            print(f"{index}. {found_item['name']} - {found_item['price']} INR - Quantity: {found_item['quantity']}")    #1. Smartphone - 17000 INR - Quantity: 1
    else:
        print(f"No items found matching '{search}'.")


# Function to update the quantity of an item in the cart
def update_quantity():
    view_cart()
    if shopping_cart:
        item_index = int(input("Enter the index of the item you want to update: ")) - 1     #1
        if 0 <= item_index < len(shopping_cart):
            new_quantity = int(input("Enter the new quantity: "))      #2
            shopping_cart[item_index]["quantity"] = new_quantity
            print("Quantity updated.\n")                               #Quantity updated.
        else:
            print("Invalid item index.\n")


# Function to remove an item from the cart
def remove_item():
    view_cart()            #Items in your shopping cart:  1. Smartphone - 17000 INR - Quantity: 2
    if shopping_cart:
        item_index = int(input("Enter the index of the item you want to remove: ")) - 1    #2
        if 0 <= item_index < len(shopping_cart):
            del shopping_cart[item_index]
            print("Item removed from the cart.\n")
        else:
            print("Invalid item index.\n")       #Invalid item index.
            
            
# Function for checkout from the cart
def checkout():
    if not shopping_cart:
        print("Your shopping cart is empty.")
    
    total_price = 0
    print("Items in your shopping cart:")      # Items in your shopping cart:
    for item in shopping_cart:
        print(f"{item['name']} - Price: {item['price']} INR - Quantity: {item['quantity']}")      # Smartphone - Price: 17000 INR - Quantity: 2
        total_price += item['price'] * item['quantity']
    
    print(f"Total Price: {total_price} INR")     #Total Price: 34000 INR
