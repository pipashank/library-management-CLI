
import json

BOOKS_FILE = "books.json"

# Load books data
def load_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save books data
def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Add a book to the library
def add_book(books):
    title = input("Enter book title: ").strip()
    quantity = int(input("Enter quantity: "))
    if title in books:
        books[title]['quantity'] += quantity
    else:
        books[title] = {"quantity": quantity}
    save_books(books)
    print(f'Book "{title}" added successfully.')

# View all books in the library
def view_books(books):
    if not books:
        print("No books available.")
        return
    print("\nAvailable Books:")
    for title, info in books.items():
        print(f'{title}: {info["quantity"]} available')
