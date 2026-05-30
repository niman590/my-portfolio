#gghag

'''adffsfsssssssssss


s
s
s
s
s
s
s
s
s
s
s
s
s
s
s
s
s
s
s
s
s
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
    
    
# Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    # Simple Library Management System
# Pure Python, terminal-based
# Approx 250 lines

import datetime

# ------------------------------
# Classes
# ------------------------------
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.year}) - Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name} - Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ------------------------------
    # Book functions
    # ------------------------------
    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
            print(f"Updated copies of {book.title}.")
        else:
            self.books[book.book_id] = book
            print(f"Added {book.title} to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Removed {removed_book.title} from library.")
        else:
            print("Book not found.")

    def search_book(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in library.")

    # ------------------------------
    # Member functions
    # ------------------------------
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member.name}")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Removed member: {removed_member.name}")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members in library.")

    # ------------------------------
    # Borrow / Return
    # ------------------------------
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies < 1:
            print(f"No copies left for {book.title}")
            return

        member.borrowed_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "borrow_date": datetime.date.today()
        })
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        borrowed_book = next((b for b in member.borrowed_books if b["book_id"] == book_id), None)

        if not borrowed_book:
            print("Book not borrowed by member.")
            return

        member.borrowed_books.remove(borrowed_book)
        self.books[book_id].copies += 1
        print(f"{member.name} returned {borrowed_book['title']}.")

    # ------------------------------
    # Reporting
    # ------------------------------
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"\n{member.name}:")
                for b in member.borrowed_books:
                    print(f" - {b['title']} borrowed on {b['borrow_date']}")
            else:
                print(f"\n{member.name} has no borrowed books.")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowed Books Report")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            copies = int(input("Copies: "))
            library.add_book(Book(book_id, title, author, year, copies))

        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "6":
            member_id = input("Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.borrowed_books_report()

        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    


'''