#!/usr/bin/python
import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
	def __init__(self):
		self.CurrentData = ""
		self.type = ""
		self.format = ""
		self.year = ""
		self.rating = ""
		self.stars = ""
		self.description = ""

	# Call when an element starts
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "movie":
			print "*****Movie*****"
			title = attributes["title"]
			print "Title:", title
	
	# Call when an elements ends
	def endElement(self, tag):
		if self.CurrentData == "type":
			print "Type:", self.type
		elif self.CurrentData == "format":
			print "Format:", self.format
		elif self.CurrentData == "year":
			print "Year:", self.year
		elif self.CurrentData == "rating":
			print "Rating:", self.rating
		elif self.CurrentData == "stars":
			print "Stars:", self.stars
		elif self.CurrentData == "description":
			print "Description:", self.description
		self.CurrentData = ""

	# Call when a character is read
	def characters(self, content):
		if self.CurrentData == "type":
			self.type = content
		elif self.CurrentData == "format":
			self.format = content
		elif self.CurrentData == "year":
			self.year = content
		elif self.CurrentData == "rating":
			self.rating = content
		elif self.CurrentData == "stars":
			self.stars = content
		elif self.CurrentData == "description":
			self.description = content

class MovietoMongo( xml.sax.ContentHandler ):
	def __init__(self):
		self.CurrentData = ""
		self.title = ""
		self.type = ""
		self.format = ""
		self.year = ""
		self.rating = ""
		self.stars = ""
		self.description = ""
		self.movies = []		

	# Call when an element starts
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "movie":
			self.title = attributes["title"]
	
	# Call when an elements ends
	def endElement(self, tag):
		self.CurrentData = tag
		if tag == "movie":
			q_movie={"title":self.title,"type":self.type,"format":self.format,"year":self.year,"rating":self.rating,"stars":self.stars,"description":self.description}
			self.movies += [q_movie]
		self.CurrentData = ""
	# Call when a character is read
	def characters(self, content):
		if self.CurrentData == "type":
			self.type = content
		elif self.CurrentData == "format":
			self.format = content
		elif self.CurrentData == "year":
			self.year = content
		elif self.CurrentData == "rating":
			self.rating = content
		elif self.CurrentData == "stars":
			self.stars = content
		elif self.CurrentData == "description":
			self.description = content

class OrderHandler( xml.sax.ContentHandler ):
	def __init__(self):
		self.CurrentData = ""
		self.customer = ""
		self.address = ""
		self.orderitemid=""
		self.sku = ""
		self.name = ""
		self.quantity = ""

	# Call when an element starts
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "order":
			print "*****ORDER*****"
			orderid = attributes["orderid"]
			print "Order ID:", orderid
		if tag == "orderitem":
			print "ORDERITEM:"
			self.total = 0

	# Call when a character is read
	def characters(self, content):	
		if self.CurrentData == "customer":
			self.customer = content
		elif self.CurrentData == "address":
			self.address = content
		elif self.CurrentData == "orderitemid":
			self.orderitemid = content
		elif self.CurrentData == "sku":
			self.sku = content
		elif self.CurrentData == "name":
			self.name = content
		elif self.CurrentData == "quantity":
			self.quantity = content
			self.total += int(self.quantity)
	
	# Call when an elements ends
	def endElement(self, tag):
		if self.CurrentData == "customer":
			print "Customer:", self.customer
		elif self.CurrentData == "address":
			print "address:", self.address
		elif self.CurrentData == "quantity":
			print "	Orderitem ID: %s, SKU: %s, Name: %s, Quantity: %s" % (self.orderitemid, self.sku, self.name, self.quantity)
		elif tag == "orderitem":
			print "	Total items: ", self.total
		self.CurrentData = ""

