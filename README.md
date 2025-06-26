# 2025-spring-Budgetingapp
This folder contains our semester project, where our group of three has designed an app aimed at helping users track their income and expenses, and monitor their budget status.
**Project overview**
The aim of this project is to develop a Budget Planning App using Python as a terminal-based application. This app will allow users to track their income and expenses and plan their budgets for various categories like rent, groceries, transport, and more over a month. It will help users allocate their resources effectively and provide insights into how well they are sticking to their planned budgets, helping them to plan better for the coming months. 
**Objective**
Work with data structures such as lists and dictionaries to manage user data.
Implement core Python concepts such as loops, conditionals, and functions.
Develop a user-friendly interface for managing budget planning and financial data.
Enable users to set budget goals and track their progress toward meeting them.
**Functional Requirements:**
**User Management:**
The system will manage users of the budget planning app. Each user will have the following details:
User ID (unique identifier for each user)
User Name
      Basic functionalities:
Add User: Existing Users can add new users by entering their name. The system will generate a unique User ID.
View Users: Displays a list of all users, showing their ID and name.
Delete User: Allows a user to be deleted by entering their User ID.

**Income Management:**
The system will manage income records, with each record containing the following:
Income ID (unique identifier for each income entry)
User ID (ID of the user who received the income)
Amount
Source (e.g., salary, freelance work)
Basic functionalities:
Log Income: Users can log new income by entering the amount and  source. A unique Income ID will be generated for each entry.
View Income: Displays a list of all income entries, showing the Income ID, User ID, Amount and  Source.
Delete Income: Users can delete an income entry by entering the Income ID.

**Expense Management:**
The system will manage expense records, with each record containing the following:
Expense ID (unique identifier for each expense entry)
User ID (ID of the user who made the expense)
Amount
Category (e.g., rent, food, transportation)
Budget limit
Basic functionalities:
Log Expense: Users can log new expenses by entering the amount and  category.  A unique Expense ID will be generated for each entry.
View Expenses: Displays a list of all expense entries, showing the Expense ID, User ID, Amount, Category, and Date(optional).
Delete Expense: Users can delete an expense entry by entering the Expense ID.

**Budget Planning:**
The core functionality of the app is to allow users to plan their budgets and compare their actual spending against these plans.
Basic functionalities:
Set Budget: Users can set budget limits for various categories (e.g., rent, groceries, entertainment). Each user can have different categories with specific budget limits.
View Budget: Displays the current budget limits and the actual spending in each category.
Track Budget Progress: The app will calculate and show users how much they have spent relative to their budget for each category.
Adjust Budget: Users can adjust their budget limits as needed.
Generate Reports: Users can generate reports showing planned vs. actual spending for this specific month, highlighting areas where they are over or under budget.
Budget Planning Record Example Structure
For the Budget Planning App, the records will be stored in a list of dictionaries. Each dictionary represents a user's financial transactions, including both income and expenses. Example structure:

**In this structure:**
User ID identifies the user.
Income is a list of dictionaries, each containing:
Income ID for the income entry.
Amount of the income received.
Source where the income originated..
Expenses is a list of dictionaries, each containing:
Expense ID for the expense entry.
Amount of the expense.
Category for the type of expense (e.g., Food, Entertainment).
Budget limit for each Category
This structure facilitates easy tracking and management of both income and expenses for each user, enabling effective budget planning and analysis.
Error handling 
Ensure the system handles missing or inaccessible CSV files gracefully.
Validate that all required data fields are present and correctly formatted.
Prevent the system from processing operations with invalid or non-existent user IDs or records.
Optional Features 
Advanced Data Structure: Use Pandas DataFrames to store user and budget data instead of lists and dictionaries for more efficient data manipulation.
Track Budget Allocations: Allow users to view their budget allocations and spending in real-time. Display detailed insights into how much has been spent versus budgeted in each category.
Search Transactions: Enable users to search for transactions by amount or category to quickly find specific entries.
Filter Transactions: Provide functionality to filter transactions by category, or amount to simplify budget analysis.
Generate Budget Reports: Offer users the option to generate detailed reports of their income, expenses, and savings for the specific month.
Set Alerts: Implement a feature to notify users when they approach or exceed their budget limits in any category.
**Technical Requirements**
The project must be developed in Python.
Students should utilize core Python concepts, including:
Variables and data types (integers, strings, floats).
Lists and dictionaries to manage budget and transaction records.
Functions to organize and modularize code.
Loops and conditionals for processing data and making decisions.
Basic file handling to save and load data from CSV files.
Implement at least one of the optional features
Provided Resources
CSV files 
User.csv : Contains User ID and User Name.
Income.csv: Contains User ID, Source of Income, and  Amount.
Expense.csv :  Contains User ID, Category, Amount Spent and Budget limit for each Category.

