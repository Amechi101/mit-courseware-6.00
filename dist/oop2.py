from oop import Point



# To represent a rectangle which is located somewhere in the XY
# plane. The question is, what information do we have to provide in order to specify such a
# rectangle?

class Rectangle:
	"""A class to manufacture rectangle ojects"""

	# Initialzer method
	def __init__( self, posn, w, h ):
		"""Initialize rectangle at posn, with width w, height h"""
		self.corner = posn
		self.width = w
		self.height = h


	def __str__(self):
		return "( {0}, {1}, {2} )".format( self.corner, self.width, self.height )

	def grow( self, delta_width, delta_height):
		"""Grow (or shrink) this object by the deltas"""
		
		#Objects are mutable! So you can change the state of an object without changing the actual position via the Class
		# example self.width = self.width + delta_width
		self.width += delta_width
		self.height += delta_height

	def move( self, dx, dy):
		"""Move this object by the deltas"""

		#Rectangle class --> corner instance --> inheriting from the Point Class x & y
		self.corner.x += dx
		self.corner.y += dy



# Using do notation to map
# box.corner.x
# box --> width & height --> corner
r = Rectangle(Point(10,5), 100, 200)
r.grow(25, -10)
r.move(35,37)


print ( r )










		