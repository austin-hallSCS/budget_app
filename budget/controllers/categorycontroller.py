from sqlalchemy import select

from budget.extensions import db
from budget.models.models import Category, Merchant, Transaction

def Get_Category_ID(name):
    result = db.session.execute(select(Category).where(Category.name == name)).first()
    if not result:
        return None
    else:
        return result[0].category_id