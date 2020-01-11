from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/happiness_db"
mongo = PyMongo(app)
# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
# Collection
country_coord = mongo.db.country_coord.find()


for country in country_coord:
    country_coord = country

# for country in country_coord.find():
#     country_coord = country

country_coord['_id'] = str(country_coord['_id'])

@app.route("/")
def index():
     country_coord = list(mongo.db.country_coord.find())
     print(country_coord)
     return render_template("index.html", country_coord = country_coord)

@app.route("/scrape")
def scrape():
    return country_coord

if __name__ == "__main__":
    app.run(debug=True)
