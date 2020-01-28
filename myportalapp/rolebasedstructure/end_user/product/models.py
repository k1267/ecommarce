
from myportalapp import db

associate_table1=db.Table('associate_table_category',
                         db.Column('catg_id',db.Integer,db.ForeignKey('category.cat_id'),primary_key=True),
                         db.Column('subcat_id',db.Integer,db.ForeignKey('subcategory.sub_id'),primary_key=True))

associate_table2=db.Table('associate_table_sub',
                          db.Column('subcat_id',db.Integer,db.ForeignKey('subcategory.sub_id'),primary_key=True),
                          db.Column('product_id', db.Integer, db.ForeignKey('product.product_id'), primary_key=True))

class Category(db.Model):
    __tablename__='category'
    cat_id=db.Column('cat_id',db.Integer,primary_key=True)
    cat_name=db.Column('cat_name',db.String(64))
    subfk=db.relationship('Subcategory',secondary=associate_table1,backref='category',lazy='joined',cascade='all,delete')

    def to_representation(self):
        subfk = [x.to_representation() for x in self.subfk]
        return {
            'cat_id':self.cat_id,
            'cat_name':self.cat_name,
            'subcategory': subfk
        }
class Subcategory(db.Model):
    __tablename__='subcategory'
    sub_id=db.Column('sub_id',db.Integer,primary_key=True)
    sub_name=db.Column('sub_name',db.String(64))
    productfk = db.relationship('Product', secondary=associate_table2, backref='subcategory', lazy='joined',
                            cascade='all,delete')
    def to_representation(self):
        productfk = [x.to_representation() for x in self.productfk]
        return{
            'sub_id':self.sub_id,
            'sub_name':self.sub_name,
            'product':productfk
        }

class Product(db.Model):
    __tablename__='product'
    product_id = db.Column('product_id', db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column('product_name', db.String(64))
    cost=db.Column('cost',db.Integer)
    avail_stock=db.Column('avail_stock',db.Integer)
    productkey=db.relationship('Cart',backref='product',lazy=True,uselist=False,cascade='all,delete')

    def to_representation(self):

        return {
        'product_id': self.product_id,
        'product_name': self.product_name,
        'cost':self.cost,
        'avail_stock':self.avail_stock
    }