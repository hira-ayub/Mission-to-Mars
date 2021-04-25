# 10.5.1 Use Flask to Create a Web App

from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# set up Flask:
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set Up App Routes
# About
@app.route("/")
#define function
def index():
   mars = mongo.db.mars.find_one()
   print(mars)
   return render_template("index.html", mars=mars)

# Scrape
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   print(mars_data)
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)


if __name__ == "__main__":
   app.run()