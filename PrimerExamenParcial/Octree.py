class Point(object):
	"""docstring for Point"""
	def __init__(self, x,y,z):
		self.x = x
		self.y = z
		self.z = z

class Rectangulo(object):
	"""docstring for Rectangulo"""
	def __init__(self, x,y,z,w,h,p):
		self.x = x
		self.y = y
		self.z = z
		self.w = w
		self.h = h
		self.p = p

	def constains(self,point):
		return (point.x >= self.x - self.w and point.x <= self.x + self.w 
		       and point.y >= self.y - self.h and point.y <= self.y + self.h 
		       and point.z >= self.z - self.p and point.z <= self.z + self.p)

	def intersect(self,range):
		return not(range.x-range.w > self.x+self.w or
				range.x+range.w < self.x+self.w or
				range.y-range.h>self.y+self.h or range.y-range.h < self.y+self.h or
				range.z-range.p > self.z+self.p or range.z+range.p <self.z+self.p)


		
		