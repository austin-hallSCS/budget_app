from sqlalchemy.sql import func

from budget.extensions import db
from budget.models.models import Category, Merchant, Transaction

def Get_All_Categories():
    result = db.session.query(Category).all()
    return result

def Get_All_Categories_Totals():
    result = db.session.query(Category.category_name, func.round(func.sum(
        Transaction.transaction_amount), 2).label("total")).group_by(
        Transaction.category_id).join(
        Transaction, Transaction.category_id == Category.category_id, isouter=True).all()
    return result
def Get_Category_ID(name):
    result = db.session.query(Category).where(Category.category_name == name).first()
    if not result:
        return None
    else:
        return result.category_id
    
def Add_Category(name):
    new_category = Category(category_name=name)
    db.session.add(new_category)
    db.session.commit()