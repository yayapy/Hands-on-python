#!/usr/etc/python

from pymongo import MongoClient
import bson

client = MongoClient() #connect to localhost:27017
db=client.mydb
#query=bson.BSON
input_id=int(raw_input("Please input id: "))

query = {'id':input_id}
qresult = db.cust_key.find(query)
print "finding key:", query
print "found", qresult.count(), "customers"

num = 1
for result in qresult:
	print "===== Customer ",num,"====="
	print "Object ID:	", result['_id']
	print "Customer id:	", result['id']
	print "Channel:	", result['channel']
	print "Customer Key:	", result['key']
	num += 1
