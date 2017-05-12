import math
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
x = int(input('x = '))
class Cl:
	def __init__(self, c1, c2, c3, c4):
		self.a = c1
		self.b = c2
		self.c = c3
		self.d = c4
class Sin (Cl):
	def __init__ (self, r1, c1, c2, c3, c4):
		Cl.__init__(self, c1, c2, c3, c4)
		self.x = r1
	def out (self):
		self.sam = (math.pow((self.a-self.x),2))+(math.pow((self.b-self.x),2))+(math.pow((self.c-self.x),2))+(math.pow((self.d-self.x),2))
		print (self.sam)

obj = Sin(x,a,b,c,d)
obj.out ()

