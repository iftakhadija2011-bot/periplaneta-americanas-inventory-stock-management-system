# Inventory & Stock Management System


# Dictionary to store all product details
stock = {}

# Function to add a new product
def add_stock():
    # Take product name as input
    name = input("Product Name: ")

    # Check if the product already exists
    if name in stock:
        print("Product Already Exists!")
    else:
        # Take quantity and price from the user
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))

        # Store product information in the dictionary
        stock[name] = {
            "quantity": quantity,
            "price": price
        }

        print("Product Added Successfully!")


# Function to display all available products
def view_products():
    # Check if the stock dictionary is not empty
    if stock:
        print("\nProduct\t\tQuantity\tPrice")

        # Display each product with its quantity and price
        for name, item in stock.items():
            print(name, "\t\t", item["quantity"], "\t\t", item["price"])
    else:
        print("No Products Available.")


# Function to increase the stock quantity
def update_stock():
    # Take product name as input
    name = input("Enter Product Name: ")

    # Check whether the product exists
    if name in stock:
        # Take the quantity to add
        add_qty = int(input("Quantity to Add: "))

        # Update the product quantity
        stock[name]["quantity"] = stock[name]["quantity"] + add_qty
        print("Stock Updated Successfully!")
    else:
        print("Product Not Found!")


# Function to update the price of a product
def update_price():
    # Take product name as input
    name = input("Enter Product Name: ")

    # Check whether the product exists
    if name in stock:
        # Take the new price
        new_price = float(input("New Price: "))

        # Update the product price
        stock[name]["price"] = new_price
        print("Price Updated Successfully!")
    else:
        print("Product Not Found!")


# Function to sell a product
def sell_item():
    # Take product name as input
    name = input("Enter Product Name: ")

    # Check whether the product exists
    if name in stock:
        # Take the quantity to sell
        sell = int(input("Quantity Sold: "))

        # Check if enough stock is available
        if sell <= stock[name]["quantity"]:
            # Reduce the stock quantity
            stock[name]["quantity"] = stock[name]["quantity"] - sell
            print("Sale Successful!")
        else:
            print("Not Enough Stock!")
    else:
        print("Product Not Found!")


# Function to check products with low stock
def check_low_stock():
    # Take the stock limit from the user
    limit = int(input("Enter low stock alert limit: "))
    found = False

    print(f"\nProducts with less than {limit} units:")

    # Search for products below the limit
    for name, item in stock.items():
        if item["quantity"] < limit:
            print(name, "-", item["quantity"])
            found = True

    # Display message if no low stock products are found
    if found == False:
        print("No Low Stock Products found under that limit.")


# Function to calculate total inventory value
def total_inventory_value():
    total = 0

    # Calculate quantity × price for every product
    for item in stock.values():
        total = total + (item["quantity"] * item["price"])

    print("Total Inventory Value =", total)


# Main menu
while True:
    # Display menu options
    print("\n===== INVENTORY & STOCK MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Stock (Quantity)")
    print("4. Update Price")
    print("5. Sell Product")
    print("6. Check Low Stock")
    print("7. Total Inventory Value")
    print("8. Exit")

    # Take user's choice
    choice = input("Enter Your Choice: ")

    # Call the Add Product function
    if choice == "1":
        add_stock()

    # Call the View Products function
    elif choice == "2":
        view_products()

    # Call the Update Stock function
    elif choice == "3":
        update_stock()

    # Call the Update Price function
    elif choice == "4":
        update_price()

    # Call the Sell Product function
    elif choice == "5":
        sell_item()

    # Call the Low Stock Check function
    elif choice == "6":
        check_low_stock()

    # Call the Total Inventory Value function
    elif choice == "7":
        total_inventory_value()

    # Exit the program
    elif choice == "8":
        print("Thank You!")
        break

    # Display error for invalid choice
    else:
        print("Invalid Choice!")