from datetime import datetime
from app import db

'''
Item ID
Item name 
Item price
Country name or ID for VAT purposes 
'''
class Item(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    item_name = db.Column(db.String(64), index=True)
    price = db.Column(db.Float, index=True)
    country_name = db.Column(db.String(128),index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) #additional field
    identifier = db.Column(db.String(64),index=True)

    def __repr__(self):
        return '<Item {}>'.format(self.id)

