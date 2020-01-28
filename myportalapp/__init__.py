from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config

db=SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    from myportalapp.rolebasedstructure.end_user.customer.views import mod as customer_module
    from myportalapp.rolebasedstructure.end_user.order.views import mod as order_module
    from myportalapp.rolebasedstructure.end_user.product.views import mod as product_module
    app.register_blueprint(customer_module)
    app.register_blueprint(order_module)
    app.register_blueprint(product_module)
    return app