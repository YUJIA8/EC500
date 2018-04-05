
# coding: utf-8

# In[7]:


import json
from pymongo import MongoClient
import pprint
import bson

client = MongoClient()
db = client.airports.database
collection = db.airports_collection

posts = db.posts


with open('airports.json') as json_file:
	new_json = json.loads(json_file.read())
	for info in new_json:
		posts.insert_one(info)

pprint.pprint(posts.find_one( { 'city': "Chengdu"}))

