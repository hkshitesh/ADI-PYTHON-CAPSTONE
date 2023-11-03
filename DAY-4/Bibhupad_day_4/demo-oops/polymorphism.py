class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        pass

    def check_availability(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, ISBN):
        super().__init__(title, author)
        self.ISBN = ISBN

    def display_info(self):
        print(f"Book Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}")

    def check_availability(self):
        return "Available"

class Magazine(LibraryItem):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def display_info(self):
        print(f"Magazine Title: {self.title}, Author: {self.author}, Issue Number: {self.issue_number}")

    def check_availability(self):
        return "Available"

class ReferenceItem(LibraryItem):
    def __init__(self, title, author, reference_number):
        super().__init__(title, author)
        self.reference_number = reference_number

    def display_info(self):
        print(f"Reference Title: {self.title}, Author: {self.author}, Reference Number: {self.reference_number}")

    def check_availability(self):
        return "For reference only"


# Demonstrate polymorphism
library_items = [
    Book("The Catcher in the Rye", "J.D. Salinger", "0316769487"),
    Magazine("National Geographic", "Various", "October 2023"),
    ReferenceItem("Encyclopedia Britannica", "Various", "REF123")
]

for item in library_items:
    item.display_info()
    print(f"Availability: {item.check_availability()}\n")
