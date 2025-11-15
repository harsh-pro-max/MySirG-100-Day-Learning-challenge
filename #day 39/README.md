# Day 39 — Data Table GUI in Python (Tkinter + Treeview)

This project is a practical demonstration of how to **display structured data in a table format** inside a desktop GUI application using **Python’s Tkinter library** and the **Treeview widget** from `ttk`.

The goal of today’s session was to understand:
- What Tkinter is,
- Why it is used,
- What Treeview is,
- And how data can be represented visually like a table seen in inventory systems or admin panels.

---

## 📘 What is Tkinter?

**Tkinter is Python’s built-in library for creating desktop GUI applications.**  
It allows you to build windows, buttons, labels, forms, tables, menus, dialogs, and much more — all using Python code.

### ✔ Key Features of Tkinter
- **Pre-installed** with Python (no separate installation needed)
- **Beginner-friendly**
- Lightweight and good for small to medium desktop tools
- Supports event-driven programming (GUI reacts to user actions)
- Works on Windows, macOS, and Linux
- Supports custom styling using `ttk` module

### ✔ Why Use Tkinter in Python?
Most Python scripts run in a **terminal**, which is not user-friendly for normal users.  
Tkinter helps convert Python programs into **interactive GUI applications** that anyone can use without knowing code.

Examples of apps you can build with Tkinter:
- Calculator  
- Inventory management tool  
- Login system  
- Form-based applications  
- Data viewer  
- Small admin dashboards  

---

## 📂 Understanding Treeview (From `ttk` Module)

To display data in **table form**, Tkinter provides the **Treeview** widget.

### ✔ What is Treeview?
Treeview is a special widget used to show:
- Tables  
- Hierarchical data  
- Multi-column lists  
- Structured datasets  

Treeview allows:
- Column headers  
- Multiple rows  
- Proper alignment  
- Scrollbars  
- Row selection  
- Formatting and styling  

### ✔ Why Treeview is important?
Normal Tkinter widgets like `Label` or `Listbox` cannot display structured multi-column data.  
Treeview makes your GUI look more professional — similar to tables seen in:
- Excel-like viewers  
- Inventory dashboards  
- Student databases  
- Product lists  

---

## 🧠 What I Learned Today

- How to create a main window using Tkinter  
- How to define columns for the table  
- How to add column headings  
- How to insert row data dynamically  
- How to center-align all the columns  
- How to format the width of each column  
- How Treeview helps in real-world GUI applications  

This session made me realize how Python GUI can be used for practical business tools like product lists, client data, school reports, etc.

---

## 💻 Full Source Code

```python
import tkinter as tk
from tkinter import ttk

data_columns = ["Item ID", "Product Name", "Price (INR)", "Stock"]

sample_data = [
    (101, "Wireless Mouse", 850, 45),
    (102, "Mechanical Keyboard", 4200, 15),
    (103, "USB-C Hub", 1500, 70),
    (104, "Laptop Stand", 990, 55),
    (105, "Monitor Cable", 450, 120)
]

def create_table_gui():
    root = tk.Tk()
    root.title("Data Table using Treeview")
    root.geometry("800x300")

    tree = ttk.Treeview(root, columns=data_columns, show='headings', height=10)

    # Define columns and headings
    for col in data_columns:
        tree.column(col, anchor=tk.CENTER, width=120)
        tree.heading(col, text=col)

    # Insert data into the table
    for item in sample_data:
        tree.insert('', tk.END, values=item)

    tree.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

    root.mainloop()

if __name__ == '__main__':
    create_table_gui()
