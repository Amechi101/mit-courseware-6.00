class Point:
	"""Point class represents and maipulates x,y coords."""
	
	# This is a initilaizer method
	def __init__(self, x=0, y=0):		
		"""Create a new point at x, y the origin and helps initialze and helps set up atributes"""
		self.x = x
		self.y = y

	#method for calculating distance from origin
	def distance_from_origin(self):
		"""Compute my distance from the origin"""
		return round(((self.x ** 2) + (self.y **2)) ** 0.5)

	def halfway(self, target):
		"""Return the halfway point between myself and the target"""
		mx = (self.x + target.x)/2
		my = (self.y + target.y)/2
		return Point(mx,my)

	#defining a string method to print 
	def __str__(self):
		return "( {0}, {1} )".format(self.x, self.y)

# p = Point(4, 2) #Instantiate an object of the type point
# q = Point(6, 3)
# r = p.halfway(q)

# #Object --> Attribute
# print (p.x, q.y, r.x, p.distance_from_origin(), p.halfway(q) )

#########

# Exercises

# ########


# # 1. Rewrite the distance function from the chapter titled Fruitful functions so that it takes
# # two Points as parameters instead of four numbers.


# class Distance:
# 	"""Distance class manipulates the x, y coordinates"""
# 	def __init__( self,  x=0, y=0 ):
# 		self.x = x
# 		self.y = y

# 	def ():
# 		pass


# # Distance Equation
# def distance(x1, y1, x2, y2):
# 	dx = x2 - x1
# 	dy = y2 - y1
# 	dsquared = dx*dx + dy*dy
# 	result = dsquared**0.5
#  	return result


# 2. Add a method reflect_x to Point which returns a new Point, one which is the
# reflection of the point about the x-axis. For example, Point(3, 5).reflect_x()
# is (3, -5)



		
		

				



	
		
		
		