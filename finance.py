with open('yourfile.html', 'r') as f:
    html_content = f.read()
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

import tkinter as tk
from tkinter import messagebox

def add_transaction(username, amount, category, note, txn_type):
    
    print(f"{txn_type.upper()} | User: {username}, Amount: {amount}, Category: {category}, Note: {note}")

def add_income_ui(parent=None, username="demo_user"):
   
    window = tk.Toplevel(parent) if parent else tk.Tk()
    window.title("Add Income")

 
    tk.Label(window, text="Amount:").pack()
    amount_entry = tk.Entry(window)
    amount_entry.pack()

    
    tk.Label(window, text="Category:").pack()
    category_entry = tk.Entry(window)
    category_entry.pack()

   
    tk.Label(window, text="Note:").pack()
    note_entry = tk.Entry(window)
    note_entry.pack()

    def submit_income():
        try:
            amount = float(amount_entry.get())
            category = category_entry.get()
            note = note_entry.get()

            if not category:
                raise ValueError("Category is required")

            add_transaction(username, amount, category, note, "income")
            messagebox.showinfo("Success", "Income added successfully!")
            window.destroy()

        except ValueError as ve:
            messagebox.showerror("Invalid Input", str(ve))

    tk.Button(window, text="Add Income", command=submit_income).pack(pady=5)

    window.mainloop() if not parent else None


add_income_ui()
