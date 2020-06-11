from flask import Flask, render_template, g, request, redirect   # This imports flask and the other things that this program needs
from flask_sqlalchemy import SQLAlchemy
# import sqlite3

# DATABASE = 'database.db'
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = 'Customer'

    Customer_ID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.Text)
    LastName = db.Column(db.Text)

class Mini(db.Model):
    __tablename__ = 'Mini'

    Car_ID = db.Column(db.Integer, primary_key=True)
    CarType = db.Column(db.Text)
    Power = db.Column(db.Integer)
    Emissions = db.Column(db.Text)
    Fuel = db.Column(db.Integer)
    Speed = db.Column(db.Integer)
    Image = db.Column(db.Text)

class Order(db.Model):
    __tablename__ = 'Order'

    Order_number = db.Column(db.Integer, primary_key=True)
    Customer_ID = db.Column(db.ForeignKey('Customer.Customer_ID'))
    Customer_name = db.Column(db.Text)
    Car_ID = db.Column(db.ForeignKey('Mini.Car_ID'))

    Mini = db.relationship('Mini', primaryjoin='Order.Car_ID == Mini.Car_ID', backref='orders')
    Customer = db.relationship('Customer', primaryjoin='Order.Customer_ID == Customer.Customer_ID', backref='orders')

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():    # this gets information from the home page file and brings it up
    return render_template('home.html')    # it tells the computer what the file is called that it needs to bring up

@app.route('/mini', methods=['GET', 'POST'])
@app.route('/mini/<int:id>')
def mini(id=None):
    minis = Mini.query.all()
    if id:
        mini = Mini.query.get_or_404(id)
        return render_template('mini_chosen.html', minis=minis, mini=mini)
    return render_template('minis.html', minis=minis)

@app.route('/mini_api/<int:id>')
def mini_api(id):
    mini = Mini.query.get_or_404(id)
    return render_template('mini_chosen.html', mini=mini)

@app.route('/bmw', methods=['GET', 'POST'])
def bmw():
    return render_template('BMW.html')

if __name__ == '__main__':    # this runs the application
    app.run(debug=True)