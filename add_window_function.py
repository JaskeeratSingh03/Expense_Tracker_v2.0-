import json 
import tkinter as tk
import os
from datetime import datetime

DATA_FILE1 = "income.json"
DATA_FILE2 = "expense.json"

# Save respective records to JSON files 
def save_record(data, record_type):
    file_name = DATA_FILE1 if record_type == "income" else DATA_FILE2
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    existing_data.append(data)

    with open(file_name, "w") as f:
        json.dump(existing_data, f, indent=4)

# Open Income Form
def open_income_form(parent):
    parent.destroy()
    income_window = tk.Tk()
    income_window.title("Add Income Record")
    income_window.geometry("400x400")
    income_window.configure(bg="#f5f5dc")
    income_window.resizable(False, False)

    tk.Label(income_window, text="Enter Income Amount:", font=("SF Pro", 14), bg="#f5f5dc").pack(pady=10)
    amount_entry = tk.Entry(income_window, font=("Arial", 14))
    amount_entry.pack(pady=10)

    tk.Label(income_window, text="Select Category:", font=("SF Pro", 14), bg="#f5f5dc").pack(pady=10)
    category_var = tk.StringVar(income_window)
    category_var.set("Salary")  # default value
    categories = ["Salary", "Business", "Investment", "Gift", "Other"]
    category_menu = tk.OptionMenu(income_window, category_var, *categories)
    category_menu.config(font=("SF Pro", 14))
    category_menu.pack(pady=10)

    def submit_income():
        amount = amount_entry.get()
        category = category_var.get()
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if amount:
            record = {
                "amount": float(amount),
                "category": category,
                "date": date_str
            }
            save_record(record, "income")
            tk.Label(income_window, text="Income record added successfully!", fg="green", bg="#f5f5dc").pack(pady=10)
            amount_entry.delete(0, tk.END)
            tk.Button(income_window, text="EXIT", font=("SF Pro", 14), command=income_window.destroy).pack(pady=20)
        else:
            tk.Label(income_window, text="Please enter a valid amount.", fg="red", bg="#f5f5dc").pack(pady=10)

    submit_button = tk.Button(income_window, text="Submit", font=("SF Pro", 14), command=submit_income)
    submit_button.pack(pady=20)

    income_window.mainloop()

# Open Expense Form
def open_expense_form(parent):
    parent.destroy()
    expense_window = tk.Tk()
    expense_window.title("Add Expense Record")
    expense_window.geometry("400x400")
    expense_window.configure(bg="#f5f5dc")
    expense_window.resizable(False, False)

    tk.Label(expense_window, text="Enter Expense Amount:", font=("SF Pro", 14), bg="#f5f5dc").pack(pady=10)
    amount_entry = tk.Entry(expense_window, font=("Arial", 14))
    amount_entry.pack(pady=10)

    tk.Label(expense_window, text="Select Category:", font=("SF Pro", 14), bg="#f5f5dc").pack(pady=10)
    category_var = tk.StringVar(expense_window)
    category_var.set("Food")  # default value
    categories = ["Food", "Transport", "Entertainment", "Bills", "Other"]
    category_menu = tk.OptionMenu(expense_window, category_var, *categories)
    category_menu.config(font=("SF Pro", 14))
    category_menu.pack(pady=10)

    def submit_expense():
        amount = amount_entry.get()
        category = category_var.get()
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if amount:
            record = {
                "amount": float(amount),
                "category": category,
                "date": date_str
            }
            save_record(record, "expense")
            tk.Label(expense_window, text="Expense record added successfully!", fg="green", bg="#f5f5dc").pack(pady=10)
            amount_entry.delete(0, tk.END)
            tk.Button(expense_window, text="EXIT", font=("SF Pro", 14), command=expense_window.destroy).pack(pady=10)
        else:
            tk.Label(expense_window, text="Please enter a valid amount.", fg="red", bg="#f5f5dc").pack(pady=10)

    submit_button = tk.Button(expense_window, text="Submit", font=("Arial", 14), command=submit_expense)
    submit_button.pack(pady=20)

    expense_window.mainloop()

# Main Window to fetch user input and bifurcate between income and expense
def AddRecordWindow():
    add_window = tk.Toplevel()
    add_window.title("Add Your Expense/Income Record")
    add_window.geometry("400x400")
    add_window.configure(bg="#f5f5dc")
    add_window.resizable(False, False)
    tk.Label(add_window, text="Select one of the options given below", font=("SF Pro", 14), bg="#f3f3cf", fg="#333333").pack(pady=20)
    tk.Button(
        add_window, 
        text="Income 💰", 
        font=("Arial", 14), 
        bg="#f5f5dc",
        command=lambda: open_income_form(add_window)
    ).pack(pady=10)
    
    tk.Button(
        add_window, 
        text="Expense 🛒", 
        font=("Arial", 14), 
        bg="#f5f5dc",
        command=lambda: open_expense_form(add_window)
    ).pack(pady=10)
