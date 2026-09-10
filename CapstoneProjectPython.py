import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
FILE_NAME = "transactions.csv"


purchases = []

while True:
    print("\nPersonal Expense Analyzer")
    print("1. Add purchase")
    print("2. View purchases")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("What did you buy? ")
        amount = float(input("How much did it cost? $"))
        category = input("What category is it? ")

        purchase = [name, amount, category]
        purchases.append(purchase)

        print("Purchase added!")

    elif choice == "2":
        print("\nYour purchases:")

        for purchase in purchases:
            print(
                purchase[0],
                "$" + str(purchase[1]),
                purchase[2]
            )

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")