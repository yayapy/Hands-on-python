#!/usr/bin/python
# Open a file
fo = open("test.py", "r+")
str1 = fo.read(10);
print "Read String is : ", str1
str2 = fo.read(10);
print "Read String again is : ", str2
# Check current position
position = fo.tell();
print "Current file position : ", position
# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str3 = fo.read(10);
print "Again read String is : ", str3
# Close opend file
fo.close()
