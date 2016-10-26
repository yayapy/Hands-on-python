#!/usr/etc/python

from pymongo import MongoClient

SRC_IP="172.31.82.43"
SRC_PORT=27017
TGT_IP="127.0.0.1"
TGT_PORT=27017

COLL_NAME="pool_customer_givex"

src = MongoClient(SRC_IP,SRC_PORT) #connect to source db @27017
tgt = MongoClient(TGT_IP,TGT_PORT) #connect to local db @27017

db_src=src.customer_master
db_tgt=tgt.mydb

src_result = db_src.system.users.find()
print src_result.count()

if src_result.count() > 0:
	tgt_ins=[]
	for sr in src_result:
		del sr['_id']
		tgt_ins+=[sr]

	tgt_result = db_tgt.system.users.insert_many(tgt_ins)
print "finished"

#pool_customer_colony_wifi
#pool_customer_esm_visionmax
#pool_customer_givex
#pool_customer_marketforce
#pool_customer_scene_bond
#pool_customer_swiss_visionmax
#pool_customer_wired_messenger

#ref_store_locations
#ref_system_names
#system.users

