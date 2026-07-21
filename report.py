import os

FILE_NAME = "products.txt"

def inventory_report():
    # Check if inventory file exists
    if not os.path.exists(FILE_NAME):
        print("\nNo inventory found.\n")
        return

    # Read all non-empty lines
    with open(FILE_NAME, "r") as file:
        products = [line.strip() for line in file if line.strip()]

    # Check if file is empty
    if not products:
        print("\nInventory is empty.\n")
        return

    total_products = 0
    total_quantity = 0

    print("\n========== Inventory Report ==========")
    print(f"{'Product':<20}{'Quantity':>10}")
    print("-" * 30)

    for product in products:
        try:
            name, quantity = product.split(",")
            quantity = int(quantity)

            print(f"{name:<20}{quantity:>10}")

            total_products += 1
            total_quantity += quantity

        except ValueError:
            print(f"Skipping invalid record: {product}")

    print("-" * 30)
    print(f"Total Product Types : {total_products}")
    print(f"Total Quantity      : {total_quantity}")
    print("=" * 30)