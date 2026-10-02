# PriceTracker

A simple terminal-based product price tracker built with Python.

## Features

* Add products with a name and price
* View all saved products
* Delete products
* Search products by name
* Sort products by price or name
* Edit existing products
* Save products to a JSON file
* Load products automatically when the program starts
* Validate product names and prices

## Requirements

* Python 3.10+ recommended
* No external libraries required

## How to Run

1. Download or clone the repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

The program will create `products.json` automatically when products are saved.

## Menu

```text
1. Add Product
2. View Products
3. Delete Product
4. Search Products
5. Sort Products
6. Edit Product
7. Exit
```

## Example

```text
=== PRICE TRACKER ===
1. Add Product
2. View Products
3. Delete Product
4. Search Products
5. Sort Products
6. Edit Product
7. Exit
Choose an option: 1

Enter product name: Apple
Enter product price: 50

Choose an option: 2

=== PRODUCTS ===
1. Apple - UAH 50.00
```

## Project Structure

```text
PriceTracker/
├── main.py
├── products.json
├── README.md
└── .gitignore
```

> `products.json` is generated automatically by the program and is used to store product data.

## What I Practiced

This project helped me practice:

* Python functions
* Lists and dictionaries
* Loops and conditional statements
* Error handling with `try/except`
* List comprehensions
* Sorting with `sorted()` and `lambda`
* File handling
* JSON serialization and deserialization
* Working with `pathlib`
* Basic input validation

## Version

**v1.0**
