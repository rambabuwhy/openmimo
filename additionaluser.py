import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
database_name = "user_database"  # Replace with your desired database name
collection_name = "additional_user"  # Replace with your desired collection name

# Create or switch to the specified database
db = client[database_name]

# Create or switch to the specified collection
collection = db[collection_name]

# Create a unique index on the "name" field
collection.create_index([("phone", pymongo.ASCENDING)], unique=True)

# Insert documents into the collection
document1 ={
    
    "username": "johndoe",
    "address": {
        "street": "123 Main St",
        "city": "Cityville",
        "state": "State",
        "zip": "12345",
        "country": "India"
    },
    "dob": "1990-01-01",
    "profile_picture": "https://example.com/profile.jpg"
}


try:
    # Insert single document
    result = collection.insert_one(document1)
    print(f"Inserted document with ID: {result.inserted_id}")

    # Insert multiple documents
    result = collection.insert_many([document1,])
    print(f"Inserted {len(result.inserted_ids)} documents with IDs: {result.inserted_ids}")

except pymongo.errors.DuplicateKeyError as e:
    print(f"Duplicate key error: {e}")
    # Handle duplicate key error as needed

except Exception as e:
    print(f"An error occurred: {e}")
    # Handle other exceptions as needed

# Query the collection
print(f"Get data from database")
query_result = collection.find({})
for document in query_result:
    print(document)

# Close the MongoDB connection
client.close()
