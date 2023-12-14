from pymongo import MongoClient
from faker import Faker
import random

# Create a Faker instance
fake = Faker()

# Establish a connection to the MongoDB server
client = MongoClient('mongodb://prcosmosmongopocsynapse:xx==@prcosmosmongopocsynapse.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@prcosmosmongopocsynapse@',)

# Select the database and collection
db = client['prdb']
collection = db['prcol']

# Insert 10 records
for _ in range(10):
    name = fake.name()
    score = random.randint(1, 100)
    record = {"name": name, "score": score}
    collection.insert_one(record)

# Close the connection
client.close()