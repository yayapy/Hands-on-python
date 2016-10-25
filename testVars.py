class testVars:
	namelst=""
	def __init__(self,var1):
		testVars.namelst=testVars.namelst+var1
	
	def prt_namelst(self):
		print testVars.namelst

v1=testVars("Var1")
v1.prt_namelst()
v2=testVars("Var2")
v2.prt_namelst()

print "%1 + %2 + %3" % "this ", "is ",  "test" 
