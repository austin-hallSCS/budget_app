from sqlalchemy import select

from budget.extensions import db
from budget.models.models import Category, Merchant, Transaction

def Get_All_Transactions_View():
    result = db.session.query(Transaction, Category).outerjoin(Category).all()
    return result

def Add_Transaction(data):
    merchants = db.session.query(Merchant, Category).outerjoin(Category).all()
