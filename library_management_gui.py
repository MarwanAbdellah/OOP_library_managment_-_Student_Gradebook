import tkinter as tk
from tkinter import messagebox
import sys
import os
import csv

class Book:
    def __init__(self, title, borrower=None):
        self.title = title
        self.borrower = borrower
        self.available = borrower is None

    def borrow(self, borrower):
        if self.available:
            self.borrower = borrower
            self.available = False
            return True
        return False

    def return_book(self):
        self.borrower = None
        self.available = True

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title):
        if title not in self.books:
            self.books[title] = Book(title)
            self.save_data()
            return True
        return False

    def borrow_book(self, title, borrower):
        if title in self.books and self.books[title].borrow(borrower):
            self.save_data()
            return True
        return False

    def return_book(self, title):
        if title in self.books and not self.books[title].available:
            self.books[title].return_book()
            self.save_data()
            return True
        return False

    def save_data(self):
        file_path = os.path.join(os.path.dirname(sys.argv[0]), "library_data.csv")
        with open(file_path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Book Title", "Borrower", "Available"])
            for title, book in self.books.items():
                writer.writerow([title, book.borrower if book.borrower else "", book.available])

library = Library()

def add_book():
    title = book_title_entry.get()
    if title:
        if library.add_book(title):
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showwarning("Error", "Book already exists!")
    book_title_entry.delete(0, tk.END)

def borrow_book():
    title = borrow_title_entry.get()
    borrower = borrower_entry.get()
    if title and borrower:
        if library.borrow_book(title, borrower):
            messagebox.showinfo("Success", "Book borrowed successfully!")
        else:
            messagebox.showwarning("Error", "Book is not available or does not exist!")
    borrow_title_entry.delete(0, tk.END)
    borrower_entry.delete(0, tk.END)

def return_book():
    title = return_title_entry.get()
    if title:
        if library.return_book(title):
            messagebox.showinfo("Success", "Book returned successfully!")
        else:
            messagebox.showwarning("Error", "Book was not borrowed or does not exist!")
    return_title_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Library Management")
root.geometry("500x350")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')

frame = tk.Frame(root)
frame.pack(expand=True, padx=20, pady=20)

# Add Book
tk.Label(frame, text="Book Title:").grid(row=0, column=0, pady=5)
book_title_entry = tk.Entry(frame, width=30)
book_title_entry.grid(row=0, column=1, pady=5)
tk.Button(frame, text="Add Book", command=add_book).grid(row=0, column=2, padx=10, pady=5)

# Warning Label
tk.Label(frame, text="Note: You must add a book before assigning its availability state.", fg="red").grid(row=1, column=0, columnspan=3, pady=5)

# Borrow Book
tk.Label(frame, text="Book Title:").grid(row=2, column=0, pady=5)
borrow_title_entry = tk.Entry(frame, width=30)
borrow_title_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Borrower:").grid(row=3, column=0, pady=5)
borrower_entry = tk.Entry(frame, width=30)
borrower_entry.grid(row=3, column=1, pady=5)

tk.Button(frame, text="Borrow Book", command=borrow_book).grid(row=4, column=0, columnspan=2, pady=10)

# Return Book
tk.Label(frame, text="Book Title:").grid(row=5, column=0, pady=5)
return_title_entry = tk.Entry(frame, width=30)
return_title_entry.grid(row=5, column=1, pady=5)

tk.Button(frame, text="Return Book", command=return_book).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()