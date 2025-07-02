from budget.extensions import db

class Income(db.Model):
    __tablename__ = "income_table"

    income_id = db.Column(db.Integer, primary_key=True)
    income_date = db.Column(db.Date, nullable=False)
    income_amount = db.Column(db.Float, nullable=False)
    income_note = db.Column(db.String(75))

class Category(db.Model):
    __tablename__ = "category_table"

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False, unique=True)
    transactions = db.relationship("Transaction", backref="category")
    merchants = db.relationship("Merchant", backref="category")

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}(category_id={self.category_id}, category_name='{self.category_name}')"

class Merchant(db.Model):
    __tablename__ = "merchant_table"

    merchant_id = db.Column(db.Integer, primary_key=True)
    merchant_name = db.Column(db.String(50), nullable=False, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category_table.category_id'))
    transactions = db.relationship("Transaction", backref="merchant")

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}(merchant_id={self.merchant_id}, merchant_name='{self.merchant_name}', category_id={self.category_id})"

    
class Transaction(db.Model):
    __tablename__ = "transaction_table"

    transaction_id = db.Column(db.Integer, primary_key=True)
    transaction_date = db.Column(db.Date, nullable=False)
    transaction_amount = db.Column(db.Float, nullable=False)
    transaction_description = db.Column(db.String(75))
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchant_table.merchant_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category_table.category_id'))

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}(transaction_id={self.transaction_id}, transaction_date={self.transaction_date}, transaction_amount={self.transaction_amount}, transaction_description='{self.transaction_description}', merchant_id={self.merchant_id}, category_id={self.category_id})"