import sys
import time
n=input("Enter: ")

#n=int(sys.argv[1],"9")
print sys.argv
if n==1:
	print "Hello World!"
	print "the end"
elif n==2:
	print "Hello Python!"
	print "the end"
else:
	print "not valid!"
	print "the end"

#text = ['t','h','i','s', 'i','s', 'a', 't','e','s','t','!']
text='this is a test'
xstr=(input("Enter a letter: "))
if (xstr in text):
	print xstr, "is in the text"
else:
	print xstr, "is not in the text"

currenttime = time.time()
localtime = time.localtime(time.time())
print "current time", currenttime
print "local time: ", localtime
