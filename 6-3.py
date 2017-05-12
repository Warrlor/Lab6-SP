import math
kg = int(input('введите kg - '))
t = int(input('введите t - '))
h = int(input('введите h - '))
class Rod:
	def __init__(self, c1, c2):
		self.kg = c1
		self.h = c2
class Sin (Rod):
	def __init__(self, r1, c1, c2):
		Rod.__init__(self, c1, c2)
		self.t = r1
	def rab(self):
		self.rabo = (self.kg + math.pow(self.h,2))/(math.pow(self.t,2))
	def out(self):
		print (self.rabo)
obj = Sin(t,kg,h)
obj.rab()
obj.out()

		

