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
geo_data = pd.read_csv("data/countries.csv")

db.country_coord.drop()
db.location_data.drop()
# Declare the collection
location_data = db.country_coord

for i in range(geo_data.shape[0]):
    post = {
        "Country": geo_data["country"][i],
        "Country Code": geo_data["code"][i],
        "Coordinates": [geo_data["Latitude"][i],geo_data["Longitude"][i]],
        "Latitude": geo_data["Latitude"][i],
        "Longitude":geo_data["Longitude"][i]
    }
    geo_data.dtypes
    location_data.insert_one(post)

#JULIA

happiness_data_2015["Year"] = '2015'
happiness_data_2016["Year"] = '2016'
happiness_data_2017["Year"] = '2017'
happiness_data_2018["Year"] = '2018'
#Renaming 2017 columns
happiness_data_2017= happiness_data_2017.rename(columns={"Happiness.Rank": "Happiness Rank", 
                                    "Happiness.Score": "Happiness Score",
                                   "Economy..GDP.per.Capita.": "Economy (GDP per Capita)",
                                    "Health..Life.Expectancy.": "Health (Life Expectancy)",
                                    "Trust..Government.Corruption.":"Trust (Government Corruption)",
                                    "Dystopia.Residual": "Dystopia Residual"
                                   })
# happiness_data_2017.columns

#Renaming 2018 columns
happiness_data_2018= happiness_data_2018.rename(columns={"Overall rank": "Happiness Rank",
                                                         "Country or region":"Country",
                                    "Score": "Happiness Score",
                                   "GDP per capita": "Economy (GDP per Capita)",
                                    "Healthy life expectancy": "Health (Life Expectancy)",
                                    "Perceptions of corruption":"Trust (Government Corruption)",
                                    "Dystopia.Residual": "Dystopia Residual",
                                                         "Freedom to make life choices": "Freedom",
                                                         "Social support":"Family"
                                   })
# happiness_data_2018.columns

db.country_coord.drop()
# Declare the collection
country_coord = db.country_coord

clean_geo = geo_data.drop(columns=['Unnamed: 0', 'country_id', 'code'])
clean_geo.head()

# Dataframes to load to database
merged_2018 = pd.merge(happiness_data_2018, clean_geo, left_on='Country', right_on='country', how='inner')
merged_2017 = pd.merge(happiness_data_2017, clean_geo, left_on='Country', right_on='country', how='inner')
merged_2016 = pd.merge(happiness_data_2016, clean_geo, left_on='Country', right_on='country', how='inner')
merged_2015 = pd.merge(happiness_data_2015, clean_geo, left_on='Country', right_on='country', how='inner')

# Combined all dataframes to verify that columns match up
merged_complete = merged_2015.append(merged_2016, ignore_index=True, sort=False)
# merged_complete.head()

merged_complete = merged_complete.append(merged_2017, ignore_index=True, sort=False)
merged_complete = merged_complete.append(merged_2018, ignore_index=True, sort=False)


merged_complete = merged_complete.sort_values(['Country','Year'])

# Remove columns: country, Region, Standard Error, Lower Confidence Interval, Upper Confidence Interval, Whisker.high, Whisker.low
cleaned_merged_complete = merged_complete.drop(columns=['Dystopia Residual','country', 'Region', 'Standard Error', 'Lower Confidence Interval', 'Upper Confidence Interval', 'Whisker.high', 'Whisker.low'])

#print(cleaned_merged_complete.head())

for i in range(cleaned_merged_complete.shape[0]):
    post = {
        "Country": cleaned_merged_complete["Country"][i],
        "Happiness Rank": int(cleaned_merged_complete["Happiness Rank"][i]),
        "Happiness Score": cleaned_merged_complete["Happiness Score"][i],
        "Economy (GDP per Capita)": cleaned_merged_complete["Economy (GDP per Capita)"][i], 
        "Family": cleaned_merged_complete["Family"][i], 
        "Health (Life Expectancy)": cleaned_merged_complete["Health (Life Expectancy)"][i],
        "Freedom": cleaned_merged_complete["Freedom"][i],
        "Trust (Government Corruption)": cleaned_merged_complete["Trust (Government Corruption)"][i], 
        "Generosity": cleaned_merged_complete["Generosity"][i],
        "Year": cleaned_merged_complete["Year"][i],
        "Latitude": cleaned_merged_complete["Latitude"][i],
        "Longitude": cleaned_merged_complete["Longitude"][i]
    }
    country_coord.insert_one(post)
