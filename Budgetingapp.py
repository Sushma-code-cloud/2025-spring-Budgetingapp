# Pandas here is used for reading and writing CSV files. It has other many purposes in data analytics.
import pandas as pd
# Matplotlib is used for plotting graphs and visualizing data. It helps us create charts to compare budgets and expenses visually.
import matplotlib.pyplot as plt
import csv
# ---------------- FILE PATHS ----------------
# Storing the file paths in variables makes it easier to change them later if needed and it saves us from repeating the same string multiple times also avoids typos.
user_file_path = "user.csv"
income_file_path = "income.csv"
expense_file_path = "expense.csv"

# ---------------- READ CSV FILES INTO DICTIONARIES ----------------
# Converting CSV files into dictionaries allows us to easily access and manipulate user, income, and expense data in our application.
# we can use dictionaries to store user information, income records, and expense entries.
user_df = pd.read_csv(user_file_path)
user_dict = user_df.to_dict(orient="records")  # List of user dictionaries 
# orient="records" means each row in the DataFrame will be converted to a dictionary, where the keys are column names and values are the corresponding row values.
# This way, we can easily access user information by their ID or name.

income_df = pd.read_csv(income_file_path)
income_dict = income_df.to_dict(orient="records")  # List of income entries

expense_df = pd.read_csv(expense_file_path)  # its okay to delete if part
if "Catergory" in expense_df.columns:
    # Fix typo in column name
    expense_df.rename(columns={"Catergory": "Category"}, inplace=True)
expense_dict = expense_df.to_dict(orient="records")  # List of expense entries

# ---------------- SESSION ----------------
current_user = None  # This will hold the currently logged-in user's data

# "global" is a built-in Python keyword that tells Python to use the variable declared outside the function.
# In simple words: it lets us remember and reuse the user info (like ID and name) after they log in
# So we can use that info in other parts of the app like income or expense functions


def login_or_register():
    global current_user
    global user_dict
    print("\n---Welcome---")
    print("1. Login with existing ID")
    print("2. Register new ID")
    choice = input("Choose an option(1 or 2): ")

    if choice == "1":  # LOGIN
        user_id = input("Enter your User ID:")
        # matched_user = none acts as a placeholder in case no matching user is found in the loop. So after the loop, you can check if a match was found:
        matched_user = None
        for user in user_dict:
            if str(user["UserID"]) == user_id:
                matched_user = user
                break

        if matched_user:
            current_user = matched_user  # saves this user info for the session
            print(f"Welcome Back. {matched_user['UserName']}!")
        else:
            print("User not found. Please try again or register first.")

    elif choice == "2":  # REGISTER
        user_id = input("Enter a new user ID: ")
        if any(str(user["UserID"]) == user_id for user in user_dict):
            print("This ID already exist. Please try logging in instead.")
            return

        user_name = input("Enter your name: ")
        new_user = {"UserID": user_id, "UserName": user_name}
        user_dict.append(new_user)
        pd.DataFrame(user_dict).to_csv(user_file_path,
                                       index=False)  # Save new user to CSV file
        # Reload updated user file to make sure data is updated in memory too
        user_df = pd.read_csv(user_file_path)
        user_dict = user_df.to_dict(orient="records")
        current_user = new_user
        print(f"User registered")

    else:
        print("Invalid choice. Please enter 1 or 2")


# ---------------- USER FUNCTIONS ----------------

def add_user():
    print("\n---Add New User---")
    new_id = int(input("Enter the new User ID:"))
    for user in user_dict:
        if user["UserID"] == new_id:
            print("Sorry, this ID already exists.")
            return
    new_name = input("Enter new user name:")
    user_dict.append({"UserID": new_id, "UserName": new_name})
    pd.DataFrame(user_dict).to_csv(user_file_path, index=False)
    print("User added successfully!.")
    print(f"Welcome, {new_name}!")


def delete_user():
    print("\n---Delete User---")
    delete_id = input("Enter the User ID to delete:").strip()
    for user in user_dict:
        user_id = str(user["UserID"]).strip()
        if user_id == delete_id:
            user_dict.remove(user)
            pd.DataFrame(user_dict).to_csv(user_file_path, index=False)
            print("User deleted successfully.")
            return
    print("User ID not found.")


def view_users():
    print("\n---Current Users---")
    df = pd.read_csv(user_file_path)
    print(df)


# ---------------- INCOME FUNCTIONS ----------------

# This simple ID generator just gives the next number (e.g., if 3 entries exist, next will be 4)
# I used len to count how many entries are already there and +1 to make a new unique ID

def generate_income_id():
    return str(len(income_dict) + 1) #we could have used max() to find the highest ID, but this is simpler and works well for our case.


def income_view():  # do we need this if not?
    if not current_user:
        print("Please log in first.")
        return
    user_id = current_user["UserID"]
    user_income = [income for income in income_dict if str(
        income.get("UserID")) == str(user_id)]
    if user_income:
        print(pd.DataFrame(user_income))
    else:
        print("No income records found.")


def add_income():
    if not current_user:
        print("Please log in first.")
        return

    print("\n--- Add New Income ---")
    income_id = generate_income_id()
    print(f"(Auto-generated Income ID: {income_id})")

    try:
        amount = float(input("Enter Income Amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    # I added capitalize() to make sure the source is consistent in format
    source = input(
        "Enter Source of Income (e.g., Salary, Gift, Freelance): ").capitalize()
    new_income = {
        "IncomeID": income_id,
        "UserID": current_user["UserID"],
        "UserName": current_user["UserName"],
        "Amount": amount,
        "Source": source
    }

    income_dict.append(new_income)
    pd.DataFrame(income_dict).to_csv(income_file_path, index=False)
    print(f"Income added for {current_user['UserName']}!")

# I added this delete_income function to allow users to remove income records by ID


def delete_income():
    if not current_user:
        print("Please log in first.")
        return
    user_id = current_user["UserID"]
    print("\n---Delete Income---")
    income_id_to_delete = input("Enter Income ID to delete: ").strip()

    for income in income_dict:
        if str(income["IncomeID"]) == income_id_to_delete and str(income["UserID"]) == str(user_id):
            income_dict.remove(income)
            pd.DataFrame(income_dict).to_csv(income_file_path, index=False)
            print("Income deleted successfully!")
            return
    print("This income ID does not belong to you. Please check and try again.")


# ---------------- EXPENSE FUNCTIONS ----------------
def generate_expense_id():
    return str(len(expense_dict) + 1)


def expense_view():
    if not current_user:
        print("Please log in first.")
        return
    print("\n--- View Expenses ---")
    user_id = current_user["UserID"]
    user_expenses = [expense for expense in expense_dict if str(
        expense.get("UserID")) == str(user_id)]
    if user_expenses:
        print("---**    Here are your expenses    **---")
        print(pd.DataFrame(user_expenses))
    else:
        # I changed a little here.
        print("Sorry, No expenses records found for this user.")


def expense_add():
    if not current_user:
        print("Please log in first.")
        return
    print("\n--- Add New Expense ---")

    expense_id = generate_expense_id()
    print(f"(Auto-generated Expense ID: {expense_id})")
    try:
        amount = float(input("Enter Expense Amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
    source = input("Enter Source of Expenses (e.g., Vacation, Gift, ): ")
    Budget = int(input("Enter the Budget for this category: "))
    expense = {
        "UserID": current_user["UserID"],
        "UserName": current_user["UserName"],
        "ExpenseID": expense_id,
        "Amount": amount,
        "Category": source.capitalize(),  # Capitalize the category for consistency
        "BudgetLimit": Budget
    }
    expense_dict.append(expense)
    df = pd.DataFrame(expense_dict)
    df.to_csv(expense_file_path, index=False)
    print("Expense added successfully")
    print(df)


def delete_expense():

    if not current_user:
        print("Please log in first.")
        return
    user_id = current_user["UserID"]
    expense_id = input("Enter the expense ID to delete: ")
    expense_id_2 = input("Re-enter the expense ID to confirm deletion: ")
    if expense_id != expense_id_2:
        print("Expense IDs do not match. Deletion cancelled.")
        return

    # Use a copy of the list to avoid modifying it while iterating
    for expense in expense_dict:
        if str(expense["ExpenseID"]) == expense_id and str(expense["UserID"]) == str(user_id):

            expense_dict.remove(expense)

            print("Expense deleted successfully.")
            df = pd.DataFrame(expense_dict)
            df.to_csv(expense_file_path, index=False)
            print(df)

            return
    print("Expense ID not found. Please check your input.")


def expense_budget_edit():
    if not current_user:
        print("Please log in first.")
        return
    user_id = current_user["UserID"]
    print("Which ExpenseID's Budget limit do you want to edit?")
    expense_id = input("Enter the Expense ID: ").strip()
    for expense in expense_dict:
        if str(expense["ExpenseID"]) == expense_id and str(expense["UserID"]) == str(user_id):
            expense["BudgetLimit"] = float(input("Enter new budget limit: "))
            pd.DataFrame(expense_dict).to_csv(expense_file_path, index=False)
            print("Budget limit updated successfully.")
            return
    else:
        print("Expense ID not found or does not belong to the current user.")


def Budget_check():
    if not current_user:
        print("Please log in first.")
        return
    user_id = current_user["UserID"]

    df = pd.read_csv("expense.csv")  # or pd.DataFrame(expenses)
    user_expenses = df[df["UserID"] == user_id]

    # Group by UserID and Category

    summary = user_expenses.groupby(["Category"]).agg({
        "Amount": "sum",
        "BudgetLimit": "first"  # Assumes budget is consistent per user per category
    }).reset_index()

# Add status column: Over or Within budget
    summary["Status"] = summary.apply(
        lambda row: "✅ Within Budget" if row["Amount"] <= row["BudgetLimit"] else "⚠️ Over Budget",
        axis=1
    )


# Display result
    print(summary)


def plot_expense_chart():
    if not current_user:
        print("Please log in first.")
        return

    user_id = current_user["UserID"]

    user_data = expense_df[expense_df["UserID"].astype(int) == user_id]
    if user_data.empty:
        print("No expense records found for this user.")
        return
    plot_data = user_data[["Category", "Amount",
                           "BudgetLimit"]].set_index("Category")
    plot_data.plot(kind="bar")
    plt.ylabel("Amount")
    plt.title("Actual vs Budget")
    plt.xticks(rotation=45)
    plt.tight_layout()  # adjusts space so it doesn't overlap
    plt.show()


# ---------------- MENUS ----------------


def main_menu():
    while True:
        print("\n--- Budget Planning System ---")
        print("1. User Management")
        print("2. Income Menu")
        print("3. Expense Menu")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")
        if choice == "1":
            user_menu()
        elif choice == "2":
            income_menu()
        elif choice == "3":
            expense_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")


def user_menu():
    while True:
        print("\n--- User Menu ---")
        print("1. Add User")
        print("2. Delete User")
        print("3. View All Users")
        print("4. Exit User Menu")
        choice = input("Enter your choice (1–4): ")
        if choice == "1":
            add_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            view_users()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")


def income_menu():
    while True:
        print("\n--- Income Menu ---")
        print("1. View All Income")
        print("2. Add New Income")
        print("3. Delete Income")
        print("4. Back to Main Menu")
        choice = input("Enter your choice (1–4): ")
        if choice == "1":
            income_view()
        elif choice == "2":
            add_income()
        elif choice == "3":
            delete_income()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")


def expense_menu():
    while True:
        print("\n--- Expense Menu ---")
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. Delete Expense")
        print("4. Edit the budget")
        print("5. Compare Budget and Actual expenses")
        print("6. Visualize Budget vs Expense")
        print("7. Back to Main Menu")
        choice = input("Enter your choice (1–7): ")
        if choice == "1":
            expense_view()
        elif choice == "2":
            expense_add()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            expense_budget_edit()
        elif choice == "5":
            Budget_check()
        elif choice == "6":
            plot_expense_chart()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    login_or_register()
    if current_user:
        main_menu()
