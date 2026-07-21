import os

FILE_NAME = "products.txt"

def search_product(name):
    if not os.path.exists(FILE_NAME):
        print("No products found.\n")
        return

    with open(FILE_NAME, "r") as file:
        for product in file:
            product_name, quantity = product.strip().split(",")

            if product_name.lower() == name.lower():
                print("\nProduct Found")
                print(f"Name: {product_name}")
                print(f"Quantity: {quantity}\n")
                return

    print("Product not found.\n")