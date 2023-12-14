from pymongo import MongoClient
import random


client = MongoClient('mongodb://prcosmosmongopocsynapse:xx==@prcosmosmongopocsynapse.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@prcosmosmongopocsynapse@',)

# Select the database and collection
db = client['prdb']
collection = db['prcol']

# Get the first 5 records
records = collection.find().limit(5)

# Update each record
for record in records:
    new_score = random.randint(1, 100)
    collection.update_one({'_id': record['_id']}, {'$set': {'score': new_score}})


# # Get the first 2 records
# records = collection.find().limit(2)

# # Delete each record
# for record in records:
#     collection.delete_one({'_id': record['_id']})