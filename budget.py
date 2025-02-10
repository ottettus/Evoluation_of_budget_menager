import csv
from dataclasses import dataclass
import pickle

import click

DB_NAME = 'budget.db'
BIG_EXPENSE = 1000

@dataclass
class ExpensesItem:
    id: int
    description: str
    amount: float

    def __post_init__(self):
        if not self.description:
            raise ValueError("Opis nie może być pusty!")
        if self.amount < BIG_EXPENSE:
            raise ValueError('Liczba nie moze byc ujemna')


def read_db() -> list[ExpensesItem]:
    try:
        with open(DB_NAME, 'rb') as stream:
            expenses = pickle.load(stream)
    except FileNotFoundError:
        expenses = []
    return expenses


def find_free_id(expenses: list[ExpensesItem]) -> int:
    counter = 1
    ids = [expense.id for expense in expenses]
    while counter in ids:
        counter += 1
    return counter


def open_expenses_from_file(filename: str) -> list[ExpensesItem]:
    try:
        with open(filename) as stream:
            reader = csv.DictReader(stream)
            expenses = []
            counter = 0
            for row in reader:
                counter += 1
                expens = ExpensesItem(
                    id=counter,
                    description=row['description'],
                    amount=float(row['amount']),
                )
                expenses.append(expens)
    except FileNotFoundError as e:
        print(f"Błąd: {e}")
        return []
    
    write_db(expenses)
    print("Pomyślnie zaimportowano!")


def write_db(update_expenses: list[ExpensesItem], overdrive: bool = False) -> None:
    with open(DB_NAME, 'wb') as stream:
        pickle.dump(update_expenses, stream)
    print('Zapisano!')

def compute_total(expenses: list[ExpensesItem]) -> float:
    amonts = [expense.amount for expense in expenses]
    return sum(amonts)

def add_new_expense(expenses: list[ExpensesItem], description: str, amount: float) -> None:
    expense = ExpensesItem(
        id=find_free_id(expenses),
        description=description,
        amount=amount,
    )
    expenses.append(expense)
    write_db(expenses)
    print('Gotowe!')


def print_report(expenses: list[ExpensesItem], total_amont: float) -> None:
    if expenses:
        print('ID | OPIS | DUŻY? | KWOTA')
        for expens in expenses:
            try:
                amount = float(expens.amount)
                is_Big = 'V' if amount > 1000 else ' '
                print(f'{expens.id:<3} | {expens.description:<20} | {is_Big:^5} | {amount:>7.2f}')
            except ValueError:
                print(f'Błąd: Wartość kwoty dla ID {expens.id} nie jest liczbą!')
        print(f' Total: {total_amont}')
    else:
        print('Nie wprowadzono zadnych wydatkow')

@click.group()
def cli():
    pass


@cli.command()
@click.argument('amount', type = float)
@click.argument('description')
def add(amount: float, description: str) -> None:
    data = read_db()
    add_new_expense(data, description, amount)


@cli.command()
def report() -> None:
    expenses = read_db()
    sum_of_amounts = compute_total(expenses)
    print_report(expenses, sum_of_amounts)


@cli.command()
def export_python() -> None:
    expenses = read_db()
    for expens in expenses:
        print(f'[ExpensesItem(id={expens.id!r}, description={expens.description!r}, amount={expens.amount})')


@cli.command()
@click.argument('location')
def import_python(location: str) -> None:
    open_expenses_from_file(location)


if __name__ == '__main__':
    cli()

