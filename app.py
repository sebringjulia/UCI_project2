from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/happiness_db"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
happiness2015Data = mongo.db.happiness_2015.find()
for country in happiness2015Data:
    print(country)

# @app.route("/")
# def index():
#     mars = mongo.db.mars.find_one()
#     return render_template("index.html", mars=mars)

'''
How to pull data using MongoDB
    Find the collection you want 
happiness2015Data = mongo.happiness_2015.find()
'''

# @app.route("/scrape")
# def scrape():
#     mars = mongo.db.mars
#     mars_data = scrape_mars.scrape_all()
#     mars.update({}, mars_data, upsert=True)
#     return "Scraping Successful!"


if __name__ == "__main__":
    app.run()
