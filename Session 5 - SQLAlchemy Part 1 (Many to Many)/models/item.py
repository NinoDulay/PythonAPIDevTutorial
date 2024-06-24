from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
 
    # Define this column/field as a foreign key
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"),unique=False, nullable=False)

    # Create another column that would contain a store
    # Define the relationship between ItemModel and StoreModel ('items' table and 'stores' table)
    store = db.relationship("StoreModel", back_populates="items")


'''
item1 = ItemModel(name="Chair", price=120, store_id=1)

item1 = {
    "id": 1,
    "name": "Chair",
    "price": 120.00,
    "store_id": 1,
    "store": {
        "id": 1,
        "name": "Furniture Store"
    }
}
'''