from flask import Flask, render_template, g, request, redirect   # This imports flask and the other things that this program needs
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():    # this gets information from the home page file and brings it up
    return render_template('home.html')    # it tells the computer what the file is called that it needs to bring up

@app.route('/mini', methods=['GET', 'POST'])
def mini():
    return render_template('minis.html')

@app.route('/bmw', methods=['GET', 'POST'])
def bmw():
    return render_template('BMW.html')

if __name__ == '__main__':    # this runs the application
    app.run(debug=True)