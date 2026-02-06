import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])

def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number for amount.")
        return
    category = input("Enter category (e.g., Food, Transport, Bills): ")
    description = input("Enter description: ")
    date_str = input("Enter date (YYYY-MM-DD) or leave empty for today: ")
    if not date_str:
        date_str = datetime.today().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Using today's date instead.")
            date_str = datetime.today().strftime("%Y-%m-%d")
    
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_str, amount, category, description])
    print("Expense added successfully!\n")

def view_expenses():
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)[1:]
        if not expenses:
            print("No expenses recorded yet.\n")
            return
        print("\nAll Expenses:")
        print(f"{'Date':<12}{'Amount':<10}{'Category':<15}{'Description'}")
        print("-"*50)
        for expense in expenses:
            date, amount, category, description = expense
            print(f"{date:<12}{amount:<10}{category:<15}{description}")
        print("-"*50 + "\n")

def view_expenses_by_category():
    category_filter = input("Enter category to filter: ")
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        expenses = [row for row in list(reader)[1:] if row[2].lower() == category_filter.lower()]
        if not expenses:
            print(f"No expenses found for category '{category_filter}'.\n")
            return
        print(f"\nExpenses in Category: {category_filter}")
        print(f"{'Date':<12}{'Amount':<10}{'Description'}")
        print("-"*40)
        for expense in expenses:
            date, amount, _, description = expense
            print(f"{date:<12}{amount:<10}{description}")
        print("-"*40 + "\n")

def view_total_expenses():
    total = 0
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)[1:]
        for expense in expenses:
            total += float(expense[1])
    print(f"\nTotal Expenses: ${total:.2f}\n")

def main_menu():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Total Expenses")
        print("5. Exit")

        choice = input("Select an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_expenses_by_category()
        elif choice == '4':
            view_total_expenses()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
