"""Web app"""
import flask
from flask import Flask, render_template, request, redirect, url_for

import pickle
import base64
from training import prediction
import requests
app = flask.Flask(__name__)

cities = [{'name':'United States', "sel": "selected"}]

model = pickle.load(open("model.pickle", 'rb'))

@app.route("/")
@app.route('/index.html')
def index() -> str:
    """Base page."""
    return flask.render_template("index.html")

@app.route('/plots.html')
def plots():
    return render_template('plots.html')

@app.route('/livemap.html')
def heatmaps():
    return render_template('livemap.html')



@app.route('/predicts.html')
def predicts():
    return render_template('predicts.html', cities=cities, cityname="Information about the city")

if __name__ == "__main__":
    app.run(debug=True)