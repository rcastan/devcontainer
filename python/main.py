import pprint
import random
from pymongo import MongoClient

print("Python devcontainer projet\n")

# Get the database connection
connection = MongoClient("mongodb://root:rbank@mongo:27017/")

# Connect to database
db = connection.library

# Printer with pretty format
pp = pprint.PrettyPrinter(indent=4)

# Connect to the collection
print('connected to mongo -> library -> inventory')


def get_all_data():
    data = list(db.inventory.find())
    print(f'\nfound {len(data)} element in the collection\n')
    pp.pprint(data)


def add_random_data():
    item = {
        "item": "random_add",
        "qty": random.randint(0, 50),
        "size": {
            "h": random.randint(10, 35),
            "w": random.randint(10, 35),
            "uom": "cm"
        },
        "status": "Z"
    }
    db.inventory.insert_one(item)
    pp.pprint(f'We just added : \n{item}')


# ---------------------------------------------------------------
# WORK
# ---------------------------------------------------------------
get_all_data()

response = input("\nDo you want to add a random data ? (y/N)")
if response.lower() == "y":
    add_random_data()
    get_all_data()

connection.close()
