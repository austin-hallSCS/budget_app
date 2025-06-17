import datetime

from flask import Blueprint, redirect, render_template, request, url_for, session

from budget.controllers.transactioncontroller import Get_All_Transactions_View, Add_Transaction
from budget.controllers.merchantcontroller import Get_All_Merchants_View
from budget.controllers.categorycontroller import Get_All_Categories_View

bp = Blueprint("transactions", __name__)

@bp.route("/", methods=("GET", "POST"))
def index():
    # Query for all transactions in db
    data = Get_All_Transactions_View()

    # Query for all merchants in db, make a list of the simplenames of each
    allmerchants = Get_All_Merchants_View()
    merchantlist = [x.simplename for x in allmerchants]

    # Query for all categories in db, make a list
    allcategories = Get_All_Categories_View()
    categorylist = [x.name for x in allcategories]

    if request.method == "POST":
        new_transaction = {"date": datetime.datetime.strptime(request.form["date"], "%Y-%m-%d"),
                           "amount": request.form["amount"],
                           "description": request.form["description"],
                           "merchant": request.form["merchant_select"],
                           "category": request.form["category_select"]}
        Add_Transaction(new_transaction)
        return redirect(url_for("transactions.index"))
        
    return render_template("transactionsview.html", transactions=data, merchants=merchantlist, categories=categorylist)