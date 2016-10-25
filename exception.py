#!/usr/bin/python
def KelvinToFahrenheit(Temperature):
	assert (Temperature >= 0),"Colder than absolute zero!"
	return ((Temperature-273)*1.8)+32

#print KelvinToFahrenheit(279)
#print int(KelvinToFahrenheit(600.78))
#print KelvinToFahrenheit(-5)

try:
	fh = open("testfile", "w")
	fh.write("This is my test file for exception handling!!")
except IOError:
	print "Error: can\'t find file or read data"
else:
	print "Written content in the file successfully"
fh.close()
