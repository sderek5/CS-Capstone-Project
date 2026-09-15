import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
FILE_NAME = "transactions.csv"


purchases = []
#Load purchases from the CSV
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            row[1] = float(row[1])
            purchases.append(row)

#Calculate Spending
def spending_summary():
    if len(purchases) == 0:
        print("\nYou don't have any purchases yet.")
        return

    total = 0

    for purchase in purchases:
        total += purchase[1]

    average = total / len(purchases)

    print("\n--- Spending Summary ---")
    print("Number of purchases:", len(purchases))
    print("Total spent: $" + str(round(total, 2)))
    print("Average purchase: $" + str(round(average, 2)))

def category_summary():
    if len(purchases) == 0:
        print("\nYou don't have any purchases yet.")
        return

    categories = {}

    for purchase in purchases:
        category = purchase[2]
        amount = purchase[1]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    total = sum(categories.values())

    print("\n--- Category Summary ---")

    for category in categories:
        amount = categories[category]
        percentage = (amount / total) * 100

        print(
            category,
            "- $" + str(round(amount, 2)),
            "- " + str(round(percentage, 1)) + "%"
        )

    highest_category = max(categories, key=categories.get)

    print("\nYou spend the most on:", highest_category)

def delete_purchase():
    if len(purchases) == 0:
        print("\nYou don't have any purchases to delete.")
        return

    print("\n--- Your Purchases ---")

    for i in range(len(purchases)):
        purchase = purchases[i]
        print(
            str(i + 1) + ".",
            purchase[0],
            "- $" + str(round(purchase[1], 2)),
            "-",
            purchase[2]
        )

    choice = int(input("\nWhich purchase do you want to delete? "))

    if choice < 1 or choice > len(purchases):
        print("Invalid choice.")
        return

    deleted = purchases.pop(choice - 1)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)

        for purchase in purchases:
            writer.writerow(purchase)

    print(deleted[0], "was deleted.")



#Main menu
while True:
    print("\nPersonal Expense Analyzer")
    print("1. Add purchase")
    print("2. View purchases")
    print("3. Spending Summary")
    print("4. View Categories")
    print("5. Delete purchase")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("What did you buy? ")
        amount = float(input("How much did it cost? $"))
        category = input("What category is it? ")

        purchase = [name, amount, category]
        purchases.append(purchase)
        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(purchase)

        print("Purchase added!")

    elif choice == "2":
        print("\n--- Your Purchases ---")

        if len(purchases) == 0:
            print("No purchases yet.")
        else:
            for purchase in purchases:
                print(
                    purchase[0],
                    "- $" + str(round(purchase[1], 2)),
                    "-",
                    purchase[2]
                )

    elif choice == "3":
        spending_summary()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        delete_purchase()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

    

