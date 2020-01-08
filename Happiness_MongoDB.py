# Dependencies
import pymongo
import pandas as pd

# Reads in HAPPINESS DATA csv files
happiness_data_2015 = pd.read_csv("data/2015.csv")
happiness_data_2016 = pd.read_csv("data/2016.csv")
happiness_data_2017 = pd.read_csv("data/2017.csv")
happiness_data_2018 = pd.read_csv("data/2018.csv")


# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Declare the database
db = client.happiness_db

db.happiness_2015.drop()
db.happiness_2016.drop()
db.happiness_2017.drop()
db.happiness_2018.drop()
# Declare the collection
happiness_2016 = db.happiness_2016
happiness_2017 = db.happiness_2017
happiness_2018 = db.happiness_2018
happiness_2015 = db.happiness_2015


for i in range(happiness_data_2015.shape[0]):
    post = {
        "Country": happiness_data_2015["Country"][i],
        "Region": happiness_data_2015["Region"][i],
        "Happiness Rank": int(happiness_data_2015["Happiness Rank"][i]),
        "Happiness Score": happiness_data_2015["Happiness Score"][i],
        "Standard Error": happiness_data_2015["Standard Error"][i],
        "Economy (GDP per Capita)": happiness_data_2015["Economy (GDP per Capita)"][i], 
        "Family": happiness_data_2015["Family"][i], 
        "Health (Life Expectancy)": happiness_data_2015["Health (Life Expectancy)"][i],
        "Freedom": happiness_data_2015["Freedom"][i],
        "Trust (Government Corruption)": happiness_data_2015["Trust (Government Corruption)"][i], 
        "Generosity": happiness_data_2015["Generosity"][i],
        "Dystopia Residual": happiness_data_2015["Dystopia Residual"][i],
        "Year": 2015
    }
    happiness_2015.insert_one(post)

for i in range(happiness_data_2016.shape[0]):
    post = {
        "Country": happiness_data_2016["Country"][i],
        "Region": happiness_data_2016["Region"][i],
        "Happiness Rank": int(happiness_data_2016["Happiness Rank"][i]),
        "Happiness Score": happiness_data_2016["Happiness Score"][i],
        "Lower Confidence Interval": happiness_data_2016["Lower Confidence Interval"][i],
        "Upper Confidence Interval": happiness_data_2016["Upper Confidence Interval"][i],
        "Economy (GDP per Capita)": happiness_data_2016["Economy (GDP per Capita)"][i], 
        "Family": happiness_data_2016["Family"][i], 
        "Health (Life Expectancy)": happiness_data_2016["Health (Life Expectancy)"][i],
        "Freedom": happiness_data_2016["Freedom"][i],
        "Trust (Government Corruption)": happiness_data_2016["Trust (Government Corruption)"][i], 
        "Generosity": happiness_data_2016["Generosity"][i],
        "Dystopia Residual": happiness_data_2016["Dystopia Residual"][i],
        "Year": "2016"
    }
    happiness_2016.insert_one(post)

for i in range(happiness_data_2017.shape[0]):
    post = {
        "Country": happiness_data_2017["Country"][i],
        "Happiness Rank": int(happiness_data_2017["Happiness.Rank"][i]),
        "Happiness Score": happiness_data_2017["Happiness.Score"][i],
        "Wisker High": happiness_data_2017["Whisker.high"][i],
        "Wisker Low": happiness_data_2017["Whisker.low"][i],
        "Economy (GDP per Capita)": happiness_data_2017["Economy..GDP.per.Capita."][i], 
        "Family": happiness_data_2017["Family"][i], 
        "Health (Life Expectancy)": happiness_data_2017["Health..Life.Expectancy."][i],
        "Freedom": happiness_data_2017["Freedom"][i],
        "Trust (Government Corruption)": happiness_data_2017["Trust..Government.Corruption."][i], 
        "Generosity": happiness_data_2017["Generosity"][i],
        "Dystopia Residual": happiness_data_2017["Dystopia.Residual"][i],
        "Year": "2017"
    }
    happiness_2017.insert_one(post)

for i in range(happiness_data_2018.shape[0]):
    post = {
        "Country": happiness_data_2018["Country or region"][i],
        "Happiness Rank": int(happiness_data_2018["Overall rank"][i]),
        "Happiness Score": happiness_data_2018["Score"][i],
        "Economy (GDP per Capita)": happiness_data_2018["GDP per capita"][i], 
        "Family": happiness_data_2018["Social support"][i], 
        "Health (Life Expectancy)": happiness_data_2018["Healthy life expectancy"][i],
        "Freedom": happiness_data_2018["Freedom to make life choices"][i],
        "Trust (Government Corruption)": happiness_data_2018["Perceptions of corruption"][i], 
        "Generosity": happiness_data_2018["Generosity"][i],
        "Year": "2018"
    }
    happiness_2018.insert_one(post)

# Adding in Latitude and Longitude Country Data
lat_long_data = pd.read_csv("data/countries.csv")

db.location.drop()
# Declare the collection
location_data = db.location_data

for i in range(lat_long_data.shape[0]):
    post = {
        "Country ID": int(lat_long_data["country_id"][i]),
        "Country": lat_long_data["country"][i],
        "Country Code": lat_long_data["code"][i],
        "Coordinates": [lat_long_data["Latitude"],lat_long_data["Longitude"]],
        "Latitude": lat_long_data["Latitude"],
        "Longitude":lat_long_data["Longitude"]
    }
    location_data.insert_one(post)
