# Importing the SQLAlchemy class from the flask_sqlalchemy module
from flask_sqlalchemy import SQLAlchemy

# Creating an instance of SQLAlchemy to interact with the database
db = SQLAlchemy()

# Defining the Item class, which will represent the 'Item' table in the database
class Item(db.Model):
    
    # Defining the 'id' column, which will serve as the primary key for each item
    id = db.Column(db.Integer, primary_key=True)  # Integer type, primary key
    
    # Defining the 'name' column, which will store the item's name
    name = db.Column(db.String(100), nullable=False)  # String type, cannot be NULL
    
    # Defining the 'description' column, which will store the item's description
    description = db.Column(db.String(200), nullable=False)  # String type, cannot be NULL
    
    # Defining the __repr__ method, which returns a string representation of the object
    def __repr__(self):
        # Returning a string that shows the id and name of the item for better readability
        return f'<Item {self.id} - {self.name}>'
