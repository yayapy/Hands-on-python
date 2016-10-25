class Employee:
	'Common base class for all employees'
	empCount = 0
	def __init__(self, name, salary):
		self.name = name 
		self.salary = salary
		Employee.empCount += 1
	def displayCount(self):
		print "Total Employee %d" % Employee.empCount
	def displayEmployee(self):
		print "Name : ", self.name, ", Salary: ", self.salary
		print "Employee.__doc__:", Employee.__doc__
		print "Employee.__name__:", Employee.__name__
		print "Employee.__module__:", Employee.__module__
		print "Employee.__bases__:", Employee.__bases__
		print "Employee.__dict__:", Employee.__dict__

class Parent: # define parent class
	parentAttr = 100
	def __init__(self):
		print "Calling parent constructor"
	def parentMethod(self):
		print 'Calling parent method'
	def setAttr(self, attr):
		Parent.parentAttr = attr
	def getAttr(self):
		print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
	def __init__(self):
		print "Calling child constructor"
	def childMethod(self):
		print 'Calling child method'
