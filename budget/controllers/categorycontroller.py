from sqlalchemy import select

from budget.extensions import db
from budget.models.models import Category, Merchant, Transaction

def Get_All_Categories_View():
    result = db.session.query(Category).all()
    return result

def Get_Category_ID(name):
    result = db.session.execute(select(Category).where(Category.name == name)).first()
    if not result:
        return None
    else:
        return result[0].category_id
    
def Add_Category(name):
    new_category = Category(name=name)
    db.session.add(new_category)
    db.session.commit()