import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
FILE_NAME = "transactions.csv"


transactions = []
budget = None

#File functions

def load_transactions():
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, mode='r', newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append({
                "name": row["name"],
                "amount": float(row["amount"]),
                "date": datetime.
            })