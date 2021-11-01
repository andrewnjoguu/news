# virtual environment first

#let us import flask 
from flask import Flask, render_template

from newsapi import NewsApiClient




app = Flask(__name__)

#route function as we render html
@app.route('/')
def home():

    newsapi = NewsApiClient(api_key="cf3fc3965f40483f84312fb87de9435b")

  #headliners

    return render_template('home.html')

if __name__ =='__main__':
    app.run(debug=True)