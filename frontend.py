import tkinter as tk
from tkinter import messagebox
import main


def add_purchase():
    name = name_entry.get()
    amount_text = amount_entry.get()
    category = category_entry.get()

    if name == "" or amount_text == "" or category == "":
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        amount = float(amount_text)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    main.add_purchase(name, amount, category)

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

    view_purchases()

    messagebox.showinfo("Success", "Purchase added!")


def view_purchases():
    purchases_box.delete(0, tk.END)

    if len(main.purchases) == 0:
        purchases_box.insert(tk.END, "No purchases yet.")
        return

    for purchase in main.purchases:
        purchases_box.insert(
            tk.END,
            purchase[0] +
            " - $" +
            str(round(purchase[1], 2)) +
            " - " +
            purchase[2]
        )


def show_spending_summary():
    result = main.spending_summary()

    messagebox.showinfo(
        "Spending Summary",
        result
    )


def show_category_summary():
    result = main.category_summary()

    messagebox.showinfo(
        "Category Summary",
        result
    )


def delete_purchase():
    selected = purchases_box.curselection()

    if not selected:
        messagebox.showerror(
            "Error",
            "Select a purchase to delete."
        )
        return

    index = selected[0]

    main.delete_purchase(index)

    view_purchases()

    messagebox.showinfo(
        "Deleted",
        "Purchase deleted!"
    )


# -------------------------
# Tkinter Frontend
# -------------------------

window = tk.Tk()

window.title("Personal Expense Analyzer")
window.geometry("700x600")


# Title
title = tk.Label(
    window,
    text="Personal Expense Analyzer",
    font=("Arial", 22, "bold")
)

title.pack(pady=20)


# Add purchase section
add_frame = tk.LabelFrame(
    window,
    text="Add Purchase",
    padx=10,
    pady=10
)

add_frame.pack(
    padx=20,
    fill="x"
)


tk.Label(
    add_frame,
    text="Purchase:"
).grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(
    add_frame,
    width=20
)

name_entry.grid(row=0, column=1, padx=5)


tk.Label(
    add_frame,
    text="Amount:"
).grid(row=0, column=2, padx=5)

amount_entry = tk.Entry(
    add_frame,
    width=12
)

amount_entry.grid(row=0, column=3, padx=5)


tk.Label(
    add_frame,
    text="Category:"
).grid(row=1, column=0, padx=5, pady=10)

category_entry = tk.Entry(
    add_frame,
    width=20
)

category_entry.grid(row=1, column=1, padx=5)


add_button = tk.Button(
    add_frame,
    text="Add Purchase",
    command=add_purchase
)

add_button.grid(
    row=1,
    column=3,
    padx=5
)


# Purchase list
tk.Label(
    window,
    text="Your Purchases",
    font=("Arial", 15, "bold")
).pack(pady=15)


purchases_box = tk.Listbox(
    window,
    width=80,
    height=13
)

purchases_box.pack(
    padx=20
)


# Buttons
button_frame = tk.Frame(window)

button_frame.pack(pady=15)


tk.Button(
    button_frame,
    text="Refresh Purchases",
    width=17,
    command=view_purchases
).grid(row=0, column=0, padx=5)


tk.Button(
    button_frame,
    text="Spending Summary",
    width=17,
    command=show_spending_summary
).grid(row=0, column=1, padx=5)


tk.Button(
    button_frame,
    text="Category Summary",
    width=17,
    command=show_category_summary
).grid(row=0, column=2, padx=5)


tk.Button(
    button_frame,
    text="Delete Selected",
    width=17,
    command=delete_purchase
).grid(row=1, column=1, pady=10)


# Show purchases when program starts
view_purchases()

window.mainloop()