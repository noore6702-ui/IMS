import os

FILE_NAME = "products.txt"

def low_stock_report(threshold=5):
    if not os.path.exists(FILE_NAME):
        print("No inventory found.\n")
        return

    with open(FILE_NAME, "r") as file:
        products = file.readlines()

    print("\n====== Low Stock Report ======")

    found = False
    for product in products:
        name, quantity = product.strip().split(",")
        quantity = int(quantity)

        if quantity <= threshold:
            print(f"{name} : {quantity}")
            found = True

    if not found:
        print("No low-stock products.")