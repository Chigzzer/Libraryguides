import tinydb
# https://media.readthedocs.org/pdf/tinydb/latest/tinydb.pdf

db = tinydb.TinyDB('test_file.json')  # creates a json database
db.insert({"Colour": "Blue", "Count": 5}) # adds the dictionary values to the json file
db.insert({"Colour": "Purple", "Count": 2})

# You can search using the .query and .search function by:
Car_colour = tinydb.Query()
# The .Query used to creat a object and use that to search
db.search(Car_colour.Colour == "Blue")
db.search(Car_colour.Count > 3)


# can update database using .update function to your query.
db.update({"Count": 4}, Car_colour.Colour == "Green")

#Use .remove to remove a piece of document
db.remove(Car_colour.Colour == "Green")


#Use .pugrge to remove all data
db.purge()