import json
from pathlib import Path

products = []
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "products.json"

def add_product():
    name = input("Enter product name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return
    try:
        price = float(input("Enter product price: "))
    except ValueError:
        print("Invalid price. Please enter a number.")
        return
    if price < 0:
        print("Price cannot be negative.")
        return
    product = {"name": name, "price": price}
    products.append(product)
    save_products()

def view_products():
    if not products:
        print("No products available.")
    else:
        print("=== PRODUCTS ===")
        for index, product in enumerate(products):
            print(f"{index + 1}. {product['name']} - UAH {product['price']:.2f}")

def delete_product():
    view_products()
    if not products:
        return
    try:
        index = int(input("Enter the product number to delete: ")) - 1
    except ValueError:
        print("Invalid product number. Please enter a number.")
        return
    if 0 <= index < len(products):
        deleted_product = products.pop(index)
        save_products()
        print(f"Deleted product: {deleted_product['name']}")
    else:
        print("Invalid product number.")

def save_products():
    with open(DB_PATH, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4, ensure_ascii=False)

def load_products():
    global products
    try:
        with open(DB_PATH, "r", encoding="utf-8") as file:
            products = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        products = []

def search_products():
    query = input("Enter product name to search: ").strip().lower()
    found_products = [product for product in products if query in product['name'].lower()]
    if not found_products:
        print("No products found.")
    else:
        print("=== SEARCH RESULTS ===")
        for index, product in enumerate(found_products):
            print(f"{index + 1}. {product['name']} - UAH {product['price']:.2f}")

def sort_products():
    if not products:
        print("No products available to sort.")
    else:
        choice = input("=== SORT PRODUCTS ===\n1. Price: Low to High\n2. Price: High to Low\n3. Name: A-Z\n4. Name: Z-A\nChoose an option: ")
        if choice == "1":
            print("=== SORTED PRODUCTS (Price: Low to High) ===")
            for product in sorted(products, key=lambda x: x['price']):
                print(f"{product['name']} - UAH {product['price']:.2f}")
        elif choice == "2":
            print("=== SORTED PRODUCTS (Price: High to Low) ===")
            for product in sorted(products, key=lambda x: x['price'], reverse=True):
                print(f"{product['name']} - UAH {product['price']:.2f}")
        elif choice == "3":
            print("=== SORTED PRODUCTS (Name: A-Z) ===")
            for product in sorted(products, key=lambda x: x['name']):
                print(f"{product['name']} - UAH {product['price']:.2f}")
        elif choice == "4":
            print("=== SORTED PRODUCTS (Name: Z-A) ===")
            for product in sorted(products, key=lambda x: x['name'], reverse=True):
                print(f"{product['name']} - UAH {product['price']:.2f}")
        else:
            print("Invalid option.")

def edit_product():
    view_products()
    if not products:
        return
    try:
        index = int(input("Enter the product number to edit: ")) - 1
    except ValueError:
        print("Invalid product number. Please enter a number. ")
        return
    if not (0 <= index < len(products)):
        print("Invalid product number.")
        return
    name = input("Enter new product name (leave blank to keep current): ").strip()
    price_input = input("Enter new product price (leave blank to keep current): ").strip()
    if price_input != "":
        try:
            price = float(price_input)
            if price < 0:
                print("Price cannot be negative.")
                return
        except ValueError:
            print("Invalid price. Please enter a number.")
            return
    if name:
        products[index]['name'] = name
    if price_input != "":
        products[index]['price'] = price
    save_products()

if __name__ == "__main__":
    load_products()
    while True:
        choose = input("=== PRICE TRACKER ===\n1. Add Product\n2. View Products\n3. Delete Product\n4. Search Products\n5. Sort Products\n6. Edit Product\n7. Exit\nChoose an option: ")
        if choose == "1":
            add_product()
        elif choose == "2":
            view_products()
        elif choose == "3":
            delete_product()
        elif choose == "4":
            search_products()
        elif choose == "5":
            sort_products()
        elif choose == "6":
            edit_product()
        elif choose == "7":
            save_products()
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")