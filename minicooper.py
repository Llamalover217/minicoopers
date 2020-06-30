# This imports flask and the other things that this program needs
from flask import Flask, render_template, g, request, redirect
from flask_sqlalchemy import SQLAlchemy
# import sqlite3

# DATABASE = 'database.db'
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'

db = SQLAlchemy(app)


# This is the Customer Model it represents the Customer table in the database :)
class Customer(db.Model):
    __tablename__ = 'Customer'

    Customer_ID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.Text)
    LastName = db.Column(db.Text)

class Mini(db.Model):   # This is the Mini model it represents the Mini table in the database
    __tablename__ = 'Mini'

    Car_ID = db.Column(db.Integer, primary_key=True)
    CarType = db.Column(db.Text)
    Power = db.Column(db.Integer)
    Emissions = db.Column(db.Text)
    Fuel = db.Column(db.Integer)
    Speed = db.Column(db.Integer)
    Image = db.Column(db.Text)


class Order(db.Model):   # This is the Order model it represents the Order table in the database
    __tablename__ = 'Order'

    Order_number = db.Column(db.Integer, primary_key=True)
    Customer_ID = db.Column(db.ForeignKey('Customer.Customer_ID'))
    Customer_name = db.Column(db.Text)
    Car_ID = db.Column(db.ForeignKey('Mini.Car_ID'))

    Mini = db.relationship(
        'Mini', primaryjoin='Order.Car_ID == Mini.Car_ID', backref='orders')
    Customer = db.relationship(
        'Customer', primaryjoin='Order.Customer_ID == Customer.Customer_ID', backref='orders')


class Bmw(db.Model):
    __tablename__ = 'Bmw'

    carID = db.Column(db.Integer, primary_key=True)
    carType = db.Column(db.Text)
    fuel = db.Column(db.Text)
    emissions = db.Column(db.Text)
    power = db.Column(db.Text)
    electricRange = db.Column(db.Text)


@app.route('/')
@app.route('/home')
def home():    # defines the home page
    # it tells the computer what the file is called that it needs to bring up
    return render_template('home.html')


@app.route('/mini')
def mini(id=None):      # This defines the mini page
    minis = Mini.query.all()
    # Says where to find the mini page
    return render_template('minis.html', minis=minis)


@app.route('/mini_api/<int:id>')
def mini_api(id):       # defines the mini car choosen
    mini = Mini.query.get_or_404(id)
    return render_template('mini_chosen.html', mini=mini)


@app.route('/bmw_api/<int:id>')
def bmw_api(id):       # defines the mini car choosen
    bmw = Bmw.query.get_or_404(id)
    return render_template('bmw_chosen.html', bmw=bmw)


@app.route('/bmw', methods=['GET', 'POST'])
def bmw():      # defines the bmw page
    bmws = Bmw.query.all()
    return render_template('BMW.html', bmws=bmws)


if __name__ == '__main__':    # this runs the application
    app.run(debug=True)
