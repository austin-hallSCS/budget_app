from sqlalchemy import select

from budget.extensions import db
from models import Category, Merchant, Transaction
from controllers import categorycontroller

def Get_All_Merchants_View():
    result = db.session.query(Merchant, Category).outerjoin(Category).all()
    return result

def Get_Merchant_ID(name):
    result = db.session.execute(select(Merchant).where(Merchant.name == name)).first()
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