# Expense Database

A Database model representation of modeling and managing financial expenses.

### Features
- Creating and adding expenses to the database
- Updating expenses
- Retrieving expenses by id and title
- Removing expense from the database
- Fetching all expenses

## Cloning the repository
- Clone this repository using `git clone <this repository git url>` in your terminal


## How to run
- After cloning the repository, change directory into the root folder of the project
```
cd expense-db
```
- In the main.py file, the Expense and ExpenseDatabase classes and uuid module has already been imported.
- Add code to utilize the ExpenseDatabase class and Expense class methods
- Run `python main.py` to test the project

### Usage
- In the main.py file, import the Expense and ExpenseDatabase classes from the expense_models module if they are not already imported.

~~~
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
~~~

- The code above can be copied to the `main.py` module and added below the `if __name__ == '__main__':` to replace the demo code already added to the section
- After adding the code and modifying as you see fit, in your terminal inside the project root folder, run `python main.py`
