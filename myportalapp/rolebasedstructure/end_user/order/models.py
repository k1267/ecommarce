from myportalapp import db


class Cart(db.Model):
    __tablename__='cart'
    cart_id=db.Column('cart_id',db.Integer,primary_key=True,autoincrement=True)
    customer_idf=db.Column('customer_idf',db.Integer,db.ForeignKey('user_table.cust_id'))
    product_idf=db.Column('product_idf',db.Integer,db.ForeignKey('product.product_id'))
    quantity_to_buy=db.Column('quantity_to_buy',db.Integer,nullable=False)
    wishlistkey=db.relationship('Wishlist',backref='cart',lazy=True,uselist=False,cascade='all,delete')
    myorderkey=db.relationship('Myorder',backref='cart',lazy=True,uselist=False,cascade='all,delete')

    def to_representation(self):
        return  {
            'customer_id':self.cutomer_id,
            'product_id':self.product_id,
            'quantity_to_buy':self.quantity_to_buy

        }

class Wishlist(db.Model):
    __tablename__='wishlist'
    wishlist_id=db.Column('wishlist_id',db.Integer,primary_key=True,autoincrement=True)
    cart_fkid=db.Column('cart_fkid',db.Integer,db.ForeignKey('cart.cart_id'))


    def to_representation(self):
        return{
            'cart_id':self.cart_id

         }

class Myorder(db.Model):
    __tablename__='myorder'
    myorder_id=db.Column('myorder_id',db.Integer,primary_key=True,autoincrement=True)
    cart_fkid=db.Column('cart_fkid',db.Integer,db.ForeignKey('cart.cart_id'))
    final_amt_to_pay=db.Column('final_amt_to_pay',db.Integer,nullable=False)

    def to_representation(self):
        return{
            'myorder_id':self.myorder_id,
            'cart_id':self.cart_id,
            'final_amt_to_pay':self.final_amt_to_pay

        }

