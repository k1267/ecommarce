from myportalapp import db
class User_table(db.Model):
    cust_id=db.Column('cust_id',db.Integer,primary_key=True,autoincrement=True)
    cust_name=db.Column('cust_name',db.String(64))
    cust_pwd=db.Column('cust_pwd',db.String(64))
    cust_address=db.Column('cust_address',db.String(100))
    cust_fk=db.relationship('Cart',backref='user_table',lazy=True,uselist=False,cascade='all,delete')
