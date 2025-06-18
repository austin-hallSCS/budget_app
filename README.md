# A simple budget app using Flask and SQLAlchemy.

Shows all transactions in the database, and has a form to add transactions.


# TO INSTALL:

## Setup
- Download the files, open in the IDE of your choice (I use VSCode so IDK if these steps will work with a different one)
- Create your .venv, install all the modules from "requirements.txt"
- Create two files inside the top-level directory: "database.db" and ".env"
    - in the .env file, add a secret key ("SECRET_KEY='YOURSECRETKEYHERE'")

## Creating/Populating DB
- Open a terminal in the top-level directory, activate the venv (.venv/scripts/activate on powershell, not sure what it is on linux/macOS)
- Open the flask shell:\
      `flask --app budget shell`
- Import the database connection:
      `from budget.extensions import db`
- Create all tables in the database:
      `db.create_all()`
- For now, you'll have to manually insert entries into the merchants and category databases. I'm working on adding default ones that populate automatically, and a way to add them through the front end.
  - First, you'll need to import the "Category" and "Merchant" model classes. and the Add functions under the "controllers" folder:
        `from budget.models.models import Category, Merchant`
        `from budget.controllers.categorycontroller import Add_Category`
        `from budget.controllers.merchantcontroller import Add_Merchant`
  - You'll need to add the categories first, as the Merchants need a 'category_id', which is linked to a row on category_table
        `Add_Category(name)`
  - The Add_Merchant function takes a dictionary as an argument
        `data = {"name": "name", "category": "category:}`
        `Add_Merchant(data)`


After setting up and creating your db, you should be good to go!
