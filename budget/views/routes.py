import datetime

from flask import Blueprint, redirect, render_template, request, url_for, session

from budget.controllers.transactioncontroller import Get_All_Transactions_View, Add_Transaction
from budget.controllers.merchantcontroller import Get_All_Merchants, Get_All_Merchants_Totals, Add_Merchant
from budget.controllers.categorycontroller import Get_All_Categories, Get_All_Categories_Totals, Add_Category

bp = Blueprint("transactions", __name__)

@bp.route("/", methods=("GET", "POST"))
def index():
    # Query for all transactions in db
    data = Get_All_Transactions_View()

    # Query for all merchants in db, make a list of the simplenames of each
    allmerchants = Get_All_Merchants()
    merchantlist = [x.merchant_name for x in allmerchants]

    # Query for all categories in db, make a list
    allcategories = Get_All_Categories()
    categorylist = [x.category_name for x in allcategories]

    if request.method == "POST":
        new_transaction = {"date": datetime.datetime.strptime(request.form["date"], "%Y-%m-%d"),
                           "amount": request.form["amount"],
                           "description": request.form["description"],
                           "merchant": request.form["merchant_select"],
                           "category": request.form["category_select"]}
        Add_Transaction(new_transaction)
        return redirect(url_for("transactions.index"))
        
    return render_template("transactionsview.html", transactions=data, merchants=merchantlist, categories=categorylist)

@bp.route("/merchants", methods=("GET", "POST"))
def merchants():
    # Query for all merchants in db, and total amount for each merchant
    data = Get_All_Merchants_Totals()

    # Query for all categories in db, make a list
    allcategories = Get_All_Categories()
    categorylist = [x.category_name for x in allcategories]

    if request.method == "POST":
        new_merchant = {"name": request.form["merchant_name"],
                        "category": request.form["category_select"]}
        Add_Merchant(new_merchant)
        return redirect(url_for("transactions.merchants"))
    
    return render_template("merchantsview.html", merchants=data, categories=categorylist)

@bp.route("/categories", methods=("GET", "POST"))
def categories():
    #Query for all categories in db, and total amount for each category
    data = Get_All_Categories_Totals()

    if request.method == "POST":
        Add_Category(request.form["category_name"])
        return redirect(url_for("transactions.categories"))
    
    return render_template("categoriesview.html", categories=data)