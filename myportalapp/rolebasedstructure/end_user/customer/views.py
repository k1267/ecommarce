from flask import Blueprint,jsonify,request
from myportalapp import db
from myportalapp.rolebasedstructure.end_user.customer.models import User_table

mod=Blueprint('customer',__name__,url_prefix='/customer')
@mod.route('',methods=['GET'])
def fetch():

 return "hi I am customer"