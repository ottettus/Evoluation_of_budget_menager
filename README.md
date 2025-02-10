Budget Manager

Project Description

A simple budget management program that allows users to track their expenses. Expense data is stored in a binary file (budget.db) using the pickle module. The program supports operations such as adding and retrieving expenses.

Features

-Add new expenses with a description and amount.
-Store data in a binary file (budget.db).
-Import expenses from a CSV file.
-Data validation (e.g., descriptions cannot be empty, amounts cannot be negative).
-Command-line interface (CLI) support using click.


Python
-pickle (for data storage)
-csv (for importing data)
-click (for CLI support)

How to Use:

Run the program in the terminal.
Add expenses by providing a description and amount.
Import expenses from a CSV file if needed.
Data is automatically saved in budget.db.