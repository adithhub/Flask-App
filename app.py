from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Item

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

# Create tables manually when running the app
def create_tables():
    with app.app_context():
        db.create_all()

# Call the function to create tables when starting the app
create_tables()

# Home route - Display all items
@app.route('/')
def home():
    items = Item.query.all()
    return render_template('home.html', items=items)

# Create new item
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_item = Item(name=name, description=description)
        db.session.add(new_item)
        db.session.commit()
        flash("Item created successfully!", "success")
        return redirect(url_for('home'))
    return render_template('edit.html', action="Create")

# Edit an existing item
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    item = Item.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        db.session.commit()
        flash("Item updated successfully!", "success")
        return redirect(url_for('home'))
    return render_template('edit.html', item=item, action="Edit")

# Delete an item
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash("Item deleted successfully!", "danger")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
