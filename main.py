import csv
import os

FILE_NAME = "transactions.csv"

purchases = []


# Load purchases from CSV
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            row[1] = float(row[1])
            purchases.append(row)


def add_purchase(name, amount, category):
    purchase = [name, amount, category]
    purchases.append(purchase)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(purchase)


def spending_summary():
    if len(purchases) == 0:
        return "You don't have any purchases yet."

    total = 0

    for purchase in purchases:
        total += purchase[1]

    average = total / len(purchases)

    return (
        "Number of purchases: " + str(len(purchases)) +
        "\nTotal spent: $" + str(round(total, 2)) +
        "\nAverage purchase: $" + str(round(average, 2))
    )


def category_summary():
    if len(purchases) == 0:
        return "You don't have any purchases yet."

    categories = {}

    for purchase in purchases:
        category = purchase[2]
        amount = purchase[1]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    total = sum(categories.values())

    result = ""

    for category in categories:
        amount = categories[category]
        percentage = (amount / total) * 100

        result += (
            category +
            " - $" + str(round(amount, 2)) +
            " - " + str(round(percentage, 1)) +
            "%\n"
        )

    highest_category = max(categories, key=categories.get)

    result += "\nYou spend the most on: " + highest_category

    return result


def delete_purchase(index):
    if index < 0 or index >= len(purchases):
        return False

    purchases.pop(index)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)

        for purchase in purchases:
            writer.writerow(purchase)

    return True