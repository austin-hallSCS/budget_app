from sqlalchemy import select

from budget.extensions import db
from budget.models.models import Transaction, Category

def Get_Transactions():
    result = db.session.query(Transaction, Category).outerjoin(Category).all()
    return result