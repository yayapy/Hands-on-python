#!/usr/etc/python

from pymongo import MongoClient
import bson

client = MongoClient("172.31.82.34",27017) #connect to localhost:27017
db=client.customer_master
#query=bson.BSON
#input_id=int(raw_input("Please input id: "))

#query = {'id':input_id}
qresult = db.pool_customer_colony_wifi.find()
#print "finding key:", query
print "found", qresult.count(), "customers"

num = 1
for result in qresult:
	print "===== Customer ",num,"====="
	print "Object ID:	", result['_id']
	print "First Name:	", result['first_name']
	print "Last Name:	", result['last_name']
	print "Email:	", result['email']
	num += 1
