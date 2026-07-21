import os

FILE_NAME = "products.txt"

def sort_products():
    if not os.path.exists(FILE_NAME):
        print("No inventory found.\n")
        return

    with open(FILE_NAME, "r") as file:
        products = []

        for line in file:
            name, quantity = line.strip().split(",")
            products.append((name, int(quantity)))

    products.sort(key=lambda x: x[1])

    print("\n====== Products Sorted by Quantity ======")
    for name, quantity in products:
        print(f"{name} : {quantity}")