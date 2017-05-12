import sys
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
class Cl:
	def __init__(self, c1, c2, c3, c4):
		self.a = c1
		self.b = c2
		self.c = c3
		self.d = c4
	def max(self):
		self.bol = [self.a, self.b, self.c, self.d]
		self.maxx = max (self.bol)
	def srarf(self):
		self.sr = (self.a + self.b + self.c + self.d)/4
	def out(self):
		print ('Самое большое число - ', self.maxx)
		print ('Среднее арифметическое - ', self.sr)
	def __del__(self):
		print ()
obj = Cl(a,b,c,d)
obj.max ()
obj.srarf ()
obj.out ()
del Cl



