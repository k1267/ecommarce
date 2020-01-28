from flask import Blueprint,jsonify,request
from myportalapp import db
from myportalapp.rolebasedstructure.end_user.order.models import Myorder,Wishlist,Cart

mod=Blueprint('order',__name__,url_prefix='/order')
@mod.route('',methods=['GET'])
def fetch():
 return "hi I am order"