from sqlalchemy import select

from budget.extensions import db
from budget.models.models import Category, Merchant, Transaction
from budget.controllers import categorycontroller
def Get_All_Merchants_View():
    result = result = db.session.execute(select(Merchant.name, Merchant.simplename, Category.name).select_from(Merchant).join(Category)).all()
    return result

def Get_Merchant_ID(name):
    result = db.session.execute(select(Merchant).where(Merchant.simplename == name)).first()
    if not result:
        return None
    else:
        return result[0].merchant_id

def Add_Merchant(data):
    existing = Get_Merchant_ID(data["name"])
    if existing != None:
        return existing
    
    new_merchant = Merchant()
    new_merchant.name = data["name"]
    new_merchant.simplename = data["simplename"]
    new_merchant.category_id = categorycontroller.Get_Category_ID(data["category"])

    db.session.add(new_merchant)
    db.session.commit()