import os

FILE_NAME = "products.txt"

def add_product(name, quantity):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{quantity}\n")
    print("Product added successfully!\n")


def view_products():
    if not os.path.exists(FILE_NAME):
        print("No products found.\n")
        return

    with open(FILE_NAME, "r") as file:
        products = file.readlines()

    if not products:
        print("No products available.\n")
        return

    print("\n------ Product List ------")
    for product in products:
        name, quantity = product.strip().split(",")
        print(f"Product: {name} | Quantity: {quantity}")