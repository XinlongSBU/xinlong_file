class Myinfo:
	def __init__(self,name = None):
		self.name = name
	
	def myinfo(self):
		if self.name:
			return "My name is "+self.name+"."
		else:
			return "I am no born yet."
