import uuid
from expense_models import Expense, ExpenseDatabase

if __name__ == '__main__':
    """
    Replace all code below with yours to test
    """
    # initialize expense database
    expense_db = ExpenseDatabase()

    # Creates an expense object with title and amount
    expense1 = Expense('School fees', 2000)

    # Updating an expense, the title and amount are optional
    expense1.update(title="Birthday party", amount=3000)

    # Fetching an expense dictionary
    expense1.to_dict()

    # Adding an expense to the database
    expense_db.add_expense(expense1)

    # Removing expense from database
    expense_db.remove_expense(expense1.id)

    # Retrieve expense by id from the database
    expense2 = Expense("Petrol", 4000)
    expense_db.add_expense(expense2)

    found_expense = expense_db.get_expense_by_id(expense2.id)
    assert found_expense.id == expense2.id, "both items are not equal"

    # Retrieve expenses by title from the database
    expenses = expense_db.get_expense_by_title(expense2.title)
    assert len(expenses) == 1, "number of items in the db does not match"

    # Retrieve expense db list of expense dictionaries
    print(expense_db.to_dict())
