import os
import pymongo



# Making Connection
myclient = MongoClient("mongodb://localhost:27017/") 

# database 
db = myclient["GenAI"]

# Created or Switched to collection 
# names: GeeksForGeeks
Collection = db["prompt"]



# Get the current directory
current_directory = os.getcwd()

# List the contents of the current directory
files = os.listdir(current_directory+"/data")

# Print the contents of the current directory
for file in files:


    # Loading or Opening the json file
    with open('data.json') as file:
        file_data = json.load(file)
        
    # Inserting the loaded data in the Collection
    # if JSON contains data more than one entry
    # insert_many is used else insert_one is used
    if isinstance(file_data, list):
        Collection.insert_one(file_data)