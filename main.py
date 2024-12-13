
from books_handler import load_books, save_books, add_book, view_books
from lend_handler import load_lends, save_lends, lend_book, return_book, datetime

def main():
    books = load_books()
    lends = load_lends()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(books)
            save_books(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            lend_book(books, lends)
            save_books(books)
        elif choice == "4":
            return_book(books, lends)
            save_books(books)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
