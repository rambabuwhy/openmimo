import pymongo

# Replace the connection string with your MongoDB server details
connection_string = "mongodb://localhost:27017"

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(connection_string)

    # Check if the connection was successful
    if client.server_info():
        print("Connected to MongoDB successfully!")
    else:
        print("Failed to connect to MongoDB.")

    # Close the connection
    client.close()

except Exception as e:
    print(f"Error: {e}")
