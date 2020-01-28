from flask import Blueprint,jsonify,request
from myportalapp import db
from myportalapp.rolebasedstructure.end_user.product.models import Category,Subcategory,Product

mod=Blueprint('product',__name__,url_prefix='/product')
@mod.route('/add_category',methods=['POST'])
def add_category():
    request_data=request.get_json()
    category=Category(
        cat_id=request_data['cat_id'],
        cat_name=request_data['cat_name'],
            )
    db.session.add(category)
    db.session.commit()
    return'category has been created'

@mod.route('/categories',methods=['GET'])
def fetch():
    category=Category.query.all()
    response = [x.to_representation() for x in category]
    return jsonify (response)

@mod.route('/add_subcategory', methods=['POST'])
def add_associate():
    request_data = request.get_json()
    cat_id=request_data['cat_id']
    subcategory= Subcategory(
            sub_id=request_data['sub_id'],
            sub_name=request_data['sub_name']

    )
    categorydetail =Category.query.get(cat_id)
    categorydetail.subfk.append(subcategory)  # Add to association table
    # use.productfk.delete(product)  # delete from association table
    # db.session.add(product)
    db.session.commit()
    return ' subcategory detail has been added.'

@mod.route('/add_product', methods=['POST'])
def add_associate_product():
    request_data = request.get_json()
    sub_id=request_data['sub_id']
    product= Product(
        product_name=request_data['product_name'],
        cost= request_data['cost'],
    avail_stock= request_data['avail_stock']


    )
    subcategorydetail =Subcategory.query.get(sub_id)
    subcategorydetail.productfk.append(product)  # Add to association table
    # use.productfk.delete(product)  # delete from association table
    # db.session.add(product)
    db.session.commit()
    return ' product detail has been added.'


@mod.route('/subcategory_product/<cid>',methods=['GET'])
def fetch_subcategory(cid):
    category=Category.query.get(int(cid))
    response = category.to_representation()
    return jsonify(response)

@mod.route('/productdetail/<sid>',methods=['GET'])
def fetch_productdetail(sid):
    subcategory=Subcategory.query.get(int(sid))
    response =subcategory.to_representation()
    return jsonify(response)

@mod.route('/product_detail',methods=['GET'])
def fetch_product_detail():
    sub_name= request.args.get('sub_name')
    subcategory= Subcategory.query.filter(Subcategory.sub_name == sub_name ).first()
    response =subcategory.to_representation()
    return jsonify(response)

'''@mod.route('/add_product', methods=['POST'])
def add_associate_product():
    request_data = request.get_json()
    sub_id=request_data['sub_id']
    product = Product(
        sub_fkid=request_data['sub_fkid'],

    )
    subcategorydetail =Subcategory.query.get(sub_id)
    subcategorydetail.productfk.append(product)  # Add to association table
    # use.productfk.delete(product)  # delete from association table
    # db.session.add(product)
    db.session.commit()
    return ' detail has been added.'

@mod.route('/add_address', methods=['POST'])
def add_address():
    request_data = request.get_json()
    student_id=request_data['student_id']
    address = Details(
        city=request_data['city'],

    )
    studentdetail = StudentInfo.query.get(student_id)
    studentdetail.addressfk.append(address)  # Add to association table
    # user.addressess.delete(address)  # delete from association table
    # db.session.add(address)
    db.session.commit()
    return 'Address detail has been added.'

@mod.route('/product/<sid>',methods=['GET'])
def fetch_product(sid):
    product=Product.query.get(int(sid))
    response = product.to_representation()
    return jsonify(response)'''