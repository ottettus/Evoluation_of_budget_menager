Budget Manager

Description

A simple command-line budget management program that allows users to track their expenses. The program supports adding, storing, and importing expenses from a CSV file. Data is saved in a binary file (budget.db) using the pickle module.

Features

Add new expenses with a description and amount
Store data in a binary file (budget.db)
Import expenses from a CSV file
Validate input data (e.g., non-empty descriptions, no negative amounts)
Command-line interface (CLI) using click
Technologies

Python
pickle (data storage)
csv (data import)
click (CLI support)
Usage

Run the program in the terminal
Add expenses by providing a description and amount
Import expenses from a CSV file if needed
Data is automatically saved in budget.db