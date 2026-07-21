import os

FILE_NAME = "products.txt"

def delete_product(product_name):
    if not os.path.exists(FILE_NAME):
        print("No inventory found.\n")
        return

    with open(FILE_NAME, "r") as file:
        products = file.readlines()

    found = False
    with open(FILE_NAME, "w") as file:
        for product in products:
            name, quantity = product.strip().split(",")
            if name.lower() != product_name.lower():
                file.write(product)
            else:
                found = True

    if found:
        print(f"{product_name} deleted successfully.")
    else:
        print("Product not found.")