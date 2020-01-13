from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/happiness_db"
mongo = PyMongo(app)
# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
# Collection


@app.route("/")
def index():
     return render_template("index.html")


@app.route("/Year")
def years():
    countries = list(mongo.db.country_coord.find({},{"_id":0}))
    Years = []
    for i in countries:
        if i['Year'] not in Years: 
            Years.append(i['Year'])
    return jsonify(Years)

@app.route("/Filter/<year>/<country>")
def filter(year,country):
    if year == '2015':
        year_filtered_data = list(mongo.db.happiness_2015.find({},{"_id":0}))
    elif year == '2016':
        year_filtered_data = list(mongo.db.happiness_2016.find({},{"_id":0}))
    elif year == '2017':
        year_filtered_data = list(mongo.db.happiness_2017.find({},{"_id":0}))
    elif year == '2018':
        year_filtered_data = list(mongo.db.happiness_2018.find({},{"_id":0}))
    else:
        year_filtered_data = list(mongo.db.country_coord.find({},{"_id":0}))
    
    if country == "All": 
        print(year_filtered_data)
        return jsonify(year_filtered_data)
    else: 
        filtered_data = []
        for i in year_filtered_data:
            if i['Country'] == country:
                filtered_data.append(i)
        print(filtered_data)
        return jsonify(filtered_data)

@app.route("/countryNames")
def country_names():
    countries = list(mongo.db.country_coord.find())
    names = []
    for i in countries:
        if i['Country'] not in names: 
            names.append(i['Country'])

    names = sorted(names)
    print(names)
    return jsonify(names)

if __name__ == "__main__":
    app.run(debug = True)
