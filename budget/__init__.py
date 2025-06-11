from flask import Flask

from budget.extensions import db


def create_app():

    app = Flask(__name__)
    app.config.from_object("config.Config")
    
    db.init_app(app)

    from .views.transactionview import bp
    app.register_blueprint(bp)

    return app