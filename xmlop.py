#!/usr/bin/python

from pymongo import MongoClient
import xml_classes
import xml.sax

if ( __name__ == "__main__"): # create an XMLReader
	parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
# override the default ContextHandler
Handler = xml_classes.MovietoMongo()
parser.setContentHandler( Handler )
parser.parse("/home/coperation/Documents/python/movies.xml")
print Handler.movies
client = MongoClient()
db=client.mydb

result=db.movies.insert_many(Handler.movies)
print result.inserted_ids

