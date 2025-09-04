import os 
import json 
import tkinter as tk

from add_window_function import AddRecordWindow

DATA_FILE1 = "income.json"
DATA_FILE2 = "expense.json"

# Help Button that guides the user
def show_help():
    help_msg = (
        "Welcome to the Expense Tracker App v2.0!\n\n"
        "1. To add a record, click on the 'Add Record' button.\n"
        "2. Choose whether to add an Income or Expense record.\n"
        "3. Fill in the required details and submit.\n"
        "4. To view records, click on the 'View Records' button.\n"
        "5. Select whether to view Income or Expense records.\n\n"
        "For further assistance, contact at my email: jaskeeratinfinity4952@gmail.com")
    custom_message(help_msg)
    
# View income or expenses records from JSON files
def view_record_entering_window():
    view_window = tk.Toplevel(root)
    view_window.title("View Records")
    view_window.geometry("400x300")
    view_window.configure(bg="#f5f5dc")
    view_window.resizable(False, False)

    tk.Label(view_window, text="Select Record Type to View:", font=("SF Pro", 14), bg="#f5f5dc").pack(pady=20)
    
    def view_records(record_type):
        file_name = DATA_FILE1 if record_type == 1 else DATA_FILE2
        nn_name = "Income" if record_type == 1 else "Expense"
        view_window = tk.Toplevel()
        view_window.title(f"View {nn_name} Records")
        view_window.geometry("500x400")
        view_window.configure(bg="#f5f5dc")

        if not os.path.exists(file_name):
            tk.Label(view_window, text="No records found.\n Did you even try adding 🙄", bg="#f5f5dc").pack(pady=20)
            return

        with open(file_name, "r") as f:
            data = json.load(f)

        for record in data:
            record_str = f"Amount: {record['amount']}, Category: {record['category']}, Date: {record['date']}"
            tk.Label(view_window, text=record_str, bg="#c9daa7").pack(pady=5)
    def on_click(record_type):
        if record_type == 1 :
            view_records(1) 
        else:
            view_records(0)
        view_window.destroy()

    income_button = tk.Button(view_window, text="💰 Income Records", font=("SF Pro", 14), bg="#c9daa7", command=lambda: on_click(1))
    income_button.pack(pady=10)

    expense_button = tk.Button(view_window, text="🛒 Expense Records", font=("SF Pro", 14), bg="#c9daa7", command=lambda: on_click(0))
    expense_button.pack(pady=10)

# custom messagebox
def custom_message(msg):
    popup = tk.Toplevel()
    popup.title("Info")
    popup.geometry("670x330")
    popup.configure(bg="#c9daa0")  

    label = tk.Label(popup, text=msg, font=("SF Pro", 14), bg="#d6e1bd")
    label.pack(pady=20)

    ok_button = tk.Button(popup, text="👌 OK", command=popup.destroy, bg="#c9daa7")
    ok_button.pack(pady=10)

# Create main window
root = tk.Tk()
root.title("Expense Tracker")

#get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Center the window
x = (screen_width // 2) - (800 // 2)
y = (screen_height // 2) - (600 // 2)

# Window size
root.geometry(f"800x600+{x}+{y}")
root.resizable(False, False)

# Set background color 
root.configure(bg="#c9daa0")  

# Title label
title = tk.Label(
    root,
    text="Expense Tracker",
    font=("SF Pro", 24, "bold"),  # formal font
    bg="#c9daa7",
    fg="#333333"   # dark text for contrast
)
title.pack(pady=10)
tk.Label(root, text="Manage your expenses and income effortlessly!", font=("SF Pro", 14), bg="#c9daa0", fg="#333333").pack(pady=50)

# View Record functionality
def view_records():
    view_window = tk.Toplevel(root)
    view_window.title("View Expense Records")
    view_window.geometry("500x400")
    view_window.configure(bg="#f5f5dc")

    if not os.path.exists("records.json"):
        tk.Label(view_window, text="No records found.\n Did you even try adding 🙄", bg="#f5f5dc").pack(pady=20)
        return

    with open("records.json", "r") as f:
        data = json.load(f)

    for record in data:
        record_str = f"Amount: {record['amount']}, Category: {record['category']}, Date: {record['date']}"
        tk.Label(view_window, text=record_str, bg="#c9daa7").pack(pady=5)

# Add Record button
add_button = tk.Button(
    root,
    text="➕ Add Record",
    font=("SF Pro", 14),
    bg="#c9daa7",   # slightly darker beige
    fg="black",
    width=15,
    height=2
)
add_button.pack(pady=20)
add_button.config(command=AddRecordWindow)

# Help button
help_button = tk.Button(
    root,
    text="❓ Help",
    font=("SF Pro", 14),
    bg="#c9daa7",
    fg="black",
    width=15,
    height=2,
    command=show_help
)
help_button.pack(pady=20)
help_button.place(relx=1.0, rely=1.0, x=-20, y=-20, anchor="se")  # bottom-right corner with some padding

# View Record button
view_button = tk.Button(
    root,
    text="📑 View Records",
    font=("SF Pro", 14),
    bg="#c9daa7",
    fg="black",
    width=15,
    height=2
)
view_button.pack(pady=30)
view_button.config(command=view_record_entering_window)

root.mainloop()

