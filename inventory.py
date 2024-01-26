# Inventory Management System

# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {}

# Function to add an item to the inventory
def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Added {quantity} of {item} to the inventory.")

# Function to view all items in the inventory
def view_inventory():
    if inventory:
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    else:
        print("The inventory is currently empty.")

# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
        print(f"The quantity of {item} has been updated to {quantity}.")
    else:
        print(f"{item} not found in the inventory.")

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            item = input("Enter the name of the item: ")
            quantity = int(input("Enter the quantity: "))
            add_item(item, quantity)
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            item = input("Enter the name of the item to update: ")
            quantity = int(input("Enter the new quantity: "))
            update_item(item, quantity)
        elif choice == '4':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()
