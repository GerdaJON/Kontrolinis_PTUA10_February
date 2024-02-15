# 2024.02.15 TEST

# Use sqlite database to save data
# Create a Finances table:
# id - primary key
# type - finance type (income/expenses)
# amount - amount of money
# category - any category (for example: Entertainment, School, Food, etc.)
# Create a console menu, where I could choose what I want to do
# Available functions:
# Enter income: I should be able to enter a sum and category of the income. It should get saved to the database
# Enter expenses: I should be able to enter a sum and category of the expense. It should get saved to the database
# Get balance: Print out the balance to the terminal (The sum of income minus the sum of expenses)
# Get all incomes: Print out the list of all incomes to the terminal (id, type, sum, category)
# Get all expenses: Print out the list of all expenses to the terminal (id, type, sum, category)
# Delete income/expense: I should be able to select any income/expense and delete it from the database (think about
# by what value you select the income/expense)
# Update income/expense: I should be able to select any income/expense and update its type (expense/income), sum,
# category. Updates should get saved to the database


import sqlite3

conn = sqlite3.connect('finances.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Finances(
    id INTEGER PRIMARY KEY,
    type TEXT,
    sum REAL,
    category TEXT
)""")

conn.commit()


def enter_income():
    amount = float(input("Enter the amount of the income: "))
    category = input("Enter the category of the income: ")
    c.execute("INSERT INTO Finances (type, sum, category) VALUES (?, ?, ?)", ("income", amount, category))
    conn.commit()
    print("Income added.")


def enter_expenses():
    amount = float(input("Enter the amount of the expense: "))
    category = input("Enter the category of the expense: ")
    c.execute("INSERT INTO Finances (type, sum, category) VALUES (?, ?, ?)", ("expense", amount, category))
    conn.commit()
    print("Expense added.")


def get_balance():
    c.execute("SELECT SUM (sum) FROM Finances WHERE type = 'income'")
    total_income = c.fetchone()[0] or 0
    c.execute("SELECT SUM (sum) FROM Finances WHERE type = 'expense'")
    total_expense = c.fetchone()[0] or 0
    balance = total_income - total_expense
    print(f"Your balance is {balance}.")


def get_all_incomes():
    c.execute("SELECT * FROM Finances WHERE type = 'income'")
    incomes = c.fetchall()
    if incomes:
        print("ID\tType\tSum\tCategory")
        for income in incomes:
            print(f'{income[0]}\t{income[1]}\t{income[2]}\t{income[3]}')
    else:
        print("No income.")


def get_all_expenses():
    c.execute("SELECT * FROM Finances WHERE type = 'expense'")
    expenses = c.fetchall()
    if expenses:
        print("ID\tType\tSum\tCategory")
        for expense in expenses:
            print(f'{expense[0]}\t{expense[1]}\t{expense[2]}\t{expense[3]}')
    else:
        print("No expenses.")


def delete_income_or_expense():
    id = int(input("Enter the id of the income or expense to delete: "))
    c.execute("SELECT * FROM Finances WHERE id = ?", (id,))
    record = c.fetchone()
    if record:
        c.execute("DELETE FROM Finances WHERE id = ?", (id,))
        conn.commit()
        print("Deleted.")
    else:
        print("Incorrect id.")


def update_income_or_expense():
    id = int(input("Enter the id of the income or expense to update: "))
    c.execute("SELECT * FROM Finances WHERE id = ?", (id,))
    record = c.fetchone()
    if record:
        type = input("Enter the new type: ")
        sum = float(input("Enter the new sum: "))
        category = input("Enter the new category: ")
        c.execute("UPDATE Finances SET type = ?, sum = ?, category = ? WHERE id = ?", (type, sum, category, id))
        conn.commit()
        print("Updated.")
    else:
        print("Incorrect id.")


def display_menu():
    print("""This is Finances app. 
    Feel free to choose from options below:
    1. Enter income
    2. Enter expense
    3. Get balance
    4. Get all incomes
    5. Get all expenses
    6. Delete income/expense
    7. Update income/expense
    8. Exit
    """)


def main():
    display_menu()
    choice = int(input("Enter your option: "))
    while choice != 8:
        if choice == 1:
            enter_income()
        elif choice == 2:
            enter_expenses()
        elif choice == 3:
            get_balance()
        elif choice == 4:
            get_all_incomes()
        elif choice == 5:
            get_all_expenses()
        elif choice == 6:
            delete_income_or_expense()
        elif choice == 7:
            update_income_or_expense()
        else:
            print("Incorrect choice.")
        display_menu()
        choice = int(input("Enter your option: "))
    print("Thank you for using the Finances app!")


if __name__ == "__main__": main()




