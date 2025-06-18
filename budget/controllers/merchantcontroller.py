from sqlalchemy.sql import func

from budget.extensions import db
from budget.models.models import Category, Merchant, Transaction
from budget.controllers import categorycontroller
def Get_All_Merchants():
    result = db.session.execute(Merchant.merchant_name, Category.category_name).join(Category, Category.category_id == Merchant.category_id, isouter=True).all()
    return result

def Get_All_Merchants_Totals():
    result = db.session.query(Merchant.merchant_name, func.round(func.sum(
        Transaction.transaction_amount), 2).label("total"), Category.category_name).group_by(
        Transaction.merchant_id).join(
        Transaction, Transaction.merchant_id == Merchant.merchant_id, isouter=True).join(
        Category, Category.category_id == Merchant.category_id, isouter=True).all()
    return result

def Get_Merchant_ID(name):
    result = db.session.query(Merchant).where(Merchant.merchant_name == name).first()
    if not result:
        return None
    else:
        return result.merchant_id

def Add_Merchant(data):
    existing = Get_Merchant_ID(data["name"])
    if existing != None:
        return existing
    
    new_merchant = Merchant()
    new_merchant.merchant_name = data["name"]
    new_merchant.category_id = categorycontroller.Get_Category_ID(data["category"])

    db.session.add(new_merchant)
    db.session.commit()