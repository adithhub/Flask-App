---

### Flask CRUD Application

This is a simple **Flask CRUD** (Create, Read, Update, Delete) application that allows users to manage a collection of items in a database. The app is built using **Flask**, **SQLAlchemy**, and **SQLite**, providing an intuitive interface to interact with the stored data. 

#### Key Features:
- **Create**: Add new items to the database with a name and description.
- **Read**: View a list of all items stored in the database.
- **Update**: Edit the name and description of existing items.
- **Delete**: Remove items from the database.

#### Technologies Used:
- **Flask**: A lightweight Python web framework that powers the app.
- **Flask-SQLAlchemy**: An extension for Flask that provides an ORM (Object-Relational Mapping) for database operations.
- **SQLite**: A simple, file-based database used to store item data.

#### Functionality:
- **Home Page**: Displays a list of all items in the database. Each item shows its name and description, and has options to edit or delete it.
- **Create Item**: A form allows the user to create new items by entering a name and description.
- **Edit Item**: Users can modify the name and description of an existing item.
- **Delete Item**: Users can delete an item from the database, which will remove it permanently.

#### Usage:
1. Clone the repository to your local machine.
2. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Access the app at `http://127.0.0.1:5000/` in your browser.
5. Use the interface to manage the items in the database.


---
