from sqlalchemy import select

from budget.extensions import db
from budget.models.models import Category, Merchant, Transaction
from budget.controllers import merchantcontroller, categorycontroller

def Get_All_Transactions_View():
    result = db.session.execute(select(Transaction.transaction_date,
                                       Transaction.transaction_amount,
                                       Transaction.transaction_description,
                                       Merchant.merchant_name,
                                       Category.category_name).select_from(Transaction).join(Category).join(Merchant)).all()
    return result

def Add_Transaction(data):
    new_transaction = Transaction()
    new_transaction.transaction_date = data["date"]
    new_transaction.transaction_amount = data["amount"]
    new_transaction.transaction_description = data["description"]
    new_transaction.merchant_id = merchantcontroller.Get_Merchant_ID(data["merchant"])
    new_transaction.category_id = categorycontroller.Get_Category_ID(data["category"])

    # If merchant does not already exist, make a new one
    if new_transaction.merchant_id == None:
        new_merchant_data = {"name": data["merchant"], "category": data["category"]}
        merchantcontroller.Add_Merchant(new_merchant_data)
        new_transaction.mercant_id = merchantcontroller.Get_Merchant_ID(data["merchant"])

    db.session.add(new_transaction)
    db.session.commit()