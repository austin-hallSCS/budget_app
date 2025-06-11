from budget.extensions import db

class Category(db.Model):
    __tablename__ = "category_table"

    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    transactions = db.relationship("Transaction", back_populates="category")

    def __repr__(self):
        return self.name

class Transaction(db.Model):
    __tablename__ = "transaction_table"

    transaction_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category_table.category_id'))
    category = db.relationship("Category", back_populates="transactions")

    def __repr__(self):
        return f"{self.date} - {self.name}: {self.amount}"