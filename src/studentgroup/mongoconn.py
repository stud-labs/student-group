from pymongo import MongoClient

CLIENT = None


def get_database():
    global CLIENT
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://192.168.191.203/studentgroup"

    # Create a connection using MongoClient.
    # You can import MongoClient or use pymongo.MongoClient
    if CLIENT is None:
        CLIENT = MongoClient(CONNECTION_STRING)

    # Create the database for our example
    # (we will use the same database throughout the tutorial
    return CLIENT['studentgroup']


# This is added so that many files can reuse the function get_database()

db = get_database()

# print("Connected: {}".format(db))

if __name__ == "__main__":

    # Get the database
    print(db)
