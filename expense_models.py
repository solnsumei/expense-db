import uuid
from datetime import datetime


class Expense:
    def __init__(self, title: str, amount: float):
        self.id = uuid.uuid4()
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update(self, title: str = None, amount: float = None):
        if title is not None:
            self.title = title

        if amount is not None:
            self.amount = amount

        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return self.__dict__

    def __repr__(self):
        """
            Helper method to return a string representation of the class
            :return: str
        """
        return str(self.__dict__)


class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
        print(f"Expense with {expense.id} added to db. Expenses in db: {len(self.expenses)}")
        return expense.id

    def remove_expense(self, expense_id):
        self.expenses = [x for x in self.expenses if x.id != expense_id]
        print(f"Expense with {expense_id} removed from db. Expenses in db: {len(self.expenses)}")

    def get_expense_by_id(self, expense_id):
        found_expenses = [x for x in self.expenses if x.id == expense_id]
        return found_expenses[0] if found_expenses else None

    def get_expense_by_title(self, expense_title):
        return [x for x in self.expenses if x.title == expense_title]

    def to_dict(self):
        return [x.to_dict() for x in self.expenses]