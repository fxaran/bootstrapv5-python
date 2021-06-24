from card import app 
from flask import Flask, render_template

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
