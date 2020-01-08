# IMPORT PYMONGO 
import pymongo

# CREATE CONNECTION (IF NOT USING LOCAL HOST)
#conn = 'mongodb://USERNAME:PASSWORD@HOST'

# CREATE CONNECTION (IF USING LOCAL HOST)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.happy_db

db.countries.insert_one(
    {
        'column1': 'test',
        'column2': 'test2',
        'column3': 'test3',
        'column4': ['test4a', 'test4b', 'test4c']
    }
)

db.locations.insert_one(
    {
        'latitude':'test_x',
        'longitude':'test_y'
    }
)