import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
''')
conn.commit()

def add_product(name, quantity, price):
    cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()

def update_product(product_id, name, quantity, price):
    cursor.execute("UPDATE products SET name=?, quantity=?, price=? WHERE id=?", (name, quantity, price, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()

def get_all_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def get_low_stock(threshold=5):
    cursor.execute("SELECT * FROM products WHERE quantity <= ?", (threshold,))
    return cursor.fetchall()

def show_inventory():
    inventory_list.delete(0, tk.END)
    for row in get_all_products():
        inventory_list.insert(tk.END, f"ID: {row[0]}, {row[1]} | Qty: {row[2]} | Price: ${row[3]}")

def add_product_gui():
    name = simpledialog.askstring("Product Name", "Enter product name:")
    quantity = simpledialog.askinteger("Quantity", "Enter quantity:")
    price = simpledialog.askfloat("Price", "Enter price:")
    if name and quantity is not None and price is not None:
        add_product(name, quantity, price)
        show_inventory()

def update_selected():
    selected = inventory_list.curselection()
    if selected:
        item = inventory_list.get(selected[0])
        product_id = int(item.split(',')[0].split(':')[1].strip())
        name = simpledialog.askstring("Update Name", "Enter new name:")
        quantity = simpledialog.askinteger("Update Quantity", "Enter new quantity:")
        price = simpledialog.askfloat("Update Price", "Enter new price:")
        if name and quantity is not None and price is not None:
            update_product(product_id, name, quantity, price)
            show_inventory()

def delete_selected():
    selected = inventory_list.curselection()
    if selected:
        item = inventory_list.get(selected[0])
        product_id = int(item.split(',')[0].split(':')[1].strip())
        delete_product(product_id)
        show_inventory()

def show_low_stock():
    low_stock = get_low_stock()
    if low_stock:
        msg = "\n".join([f"{item[1]}: {item[2]} in stock" for item in low_stock])
    else:
        msg = "No low-stock items."
    messagebox.showinfo("Low Stock Alert", msg)

root = tk.Tk()
root.title("Inventory Management System")

tk.Button(root, text="Add Product", command=add_product_gui).pack(pady=5)
tk.Button(root, text="Edit Selected", command=update_selected).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_selected).pack(pady=5)
tk.Button(root, text="Show Low Stock", command=show_low_stock).pack(pady=5)
tk.Button(root, text="Refresh List", command=show_inventory).pack(pady=5)

inventory_list = tk.Listbox(root, width=60)
inventory_list.pack(pady=10)
show_inventory()

root.mainloop()
