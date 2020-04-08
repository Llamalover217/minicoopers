from flask import Flask, render_template, g, request, redirect   # This imports flask and the other things that this program needs
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():    # this gets information from the home page file and brings it up
    return render_template('home.html')    # it tells the computer what the file is called that it needs to bring up

if __name__ == '__main__':    # this runs the application
    app.run(debug=True)