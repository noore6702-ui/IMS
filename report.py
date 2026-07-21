import os

FILE_NAME = "products.txt"

def inventory_report():
    if not os.path.exists(FILE_NAME):
        print("No inventory found.\n")
        return

    with open(FILE_NAME, "r") as file:
        products = file.readlines()

    total_products = len(products)
    total_quantity = 0

    for product in products:
        _, quantity = product.strip().split(",")
        total_quantity += int(quantity)

    print("\n====== Inventory Report ======")
    print(f"Total Product Types : {total_products}")
    print(f"Total Quantity      : {total_quantity}")