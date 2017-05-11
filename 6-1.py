import math
x = int(input('Введите x '))
y = int(input('Введите y '))
class lon(object):
	"""docstring for lon"""
	def __init__(self, r1, r2):
		self.x = r1
		self.y = r2
	def chet (self):
		self.rast = math.sqrt(math.pow(self.x,2)+math.pow(self.y,2))
	def prin (self):
		print ('Расстояние до начала координат - ',self.rast)
obj = lon(x,y)
obj.chet()
obj.prin()
		
