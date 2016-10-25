def changeme(pmylist):
	ilist=[5,6,7,8]
	pmylist += ilist;
	print "Values inside the function:", pmylist
	return
def changeme2(pmylist):
	print "first Values inside the function: ", pmylist
	in_mylist = ['A','B','C','D']
	pmylist = in_mylist + ['E','F','G','H']
	print "2nd Values inside the function: ", pmylist
	return

print "////////////////////////////////"
mylist = [1,2,3,4]
print "Original list:", mylist
changeme(mylist);
print "Updated list:", mylist
print "==============================="
mylist2 = [11,12,13,14]
changeme2(mylist2);
print "Values outside the function: ", mylist2
print "////////////////////////////////"
