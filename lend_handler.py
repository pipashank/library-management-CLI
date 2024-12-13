
import json
from datetime import datetime, timedelta

LEND_FILE = "lend.json"

# Load lending data
def load_lends():
    try:
        with open(LEND_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save lending data
def save_lends(lends):
    with open(LEND_FILE, "w") as file:
        json.dump(lends, file, indent=4)

# Lend a book
def lend_book(books, lends):
    title = input("Enter the book title to lend: ").strip()
    if title not in books or books[title]['quantity'] <= 0:
        print("There are not enough books available to lend.")
        return

    name = input("Enter borrower's name: ").strip()
    phone = input("Enter borrower's phone number: ").strip()
    due_date = datetime.now() + timedelta(days=14)

    # Update lend information
    lends[title] = lends.get(title, [])
    lends[title].append({
        "name": name,
        "phone": phone,
        "due_date": due_date.strftime("%Y-%m-%d")
    })
    books[title]['quantity'] -= 1

    save_lends(lends)
    print(f'Book "{title}" lent to {name}. Return due by {due_date.strftime("%Y-%m-%d")}.')

# Return a book
def return_book(books, lends):
    title = input("Enter the book title to return: ").strip()
    if title not in lends or not lends[title]:
        print("No one has borrowed this book.")
        return

    name = input("Enter the borrower's name: ").strip()
    borrower_found = False

    for borrower in lends[title]:
        if borrower['name'] == name:
            lends[title].remove(borrower)
            books[title]['quantity'] += 1
            borrower_found = True
            print(f'Book "{title}" returned by {name}.')
            break

    if not borrower_found:
        print("Borrower not found.")

    save_lends(lends)
