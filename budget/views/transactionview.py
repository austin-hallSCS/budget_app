from flask import Blueprint, redirect, render_template, request, url_for, session

from budget.controllers.transactioncontroller import Get_Transactions

bp = Blueprint("transactions", __name__)

@bp.route("/")
def index():
    data = Get_Transactions()
    return render_template("transactionsview.html", transactions=data)