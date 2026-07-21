import os

FILE_NAME = "products.txt"

def update_quantity(product_name, new_quantity):
    if not os.path.exists(FILE_NAME):
        print("No inventory found.\n")
        return

    with open(FILE_NAME, "r") as file:
        products = file.readlines()

    found = False
    with open(FILE_NAME, "w") as file:
        for product in products:
            name, quantity = product.strip().split(",")
            if name.lower() == product_name.lower():
                file.write(f"{name},{new_quantity}\n")
                found = True
            else:
                file.write(product)

    if found:
        print(f"{product_name} quantity updated successfully.")
    else:
        print("Product not found.")