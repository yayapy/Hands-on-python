#!/usr/etc/python

from pymongo import MongoClient
import bson

client = MongoClient() #connect to localhost:27017
db=client.mydb
#query=bson.BSON
query_all=[]
for i in range(30000):
	str_id=i+240
	str_key=str(str_id)+"@python"+str(str_id)+".com"
	query={"id":str_id,"channel":"G","key":str_key}
	query_all+=[query]
	#data = bson.BSON.encode(query)

qresult = db.cust_key.insert_many(query_all)
#print qresult.inserted_ids
#print query_all 
print "Insert finished"
