from oop import Point


# Even thou they contain the same corrdinates, they are not the same object, resulting in a check of false
# This is called a shallow equality, as it compares only references not the contents of the objects.
p1 = Point(3,4)
p2 = Point(3,4)

if p1 is p2:
	print(True)
else:
	print(False)

# p1 is p3 so it equates to True
# p3 = p1

# To compare the contents of the objects deep equality we can write a function called
# same_coordinates



def same_coordinates( p3, p4 ):


	return (p3.x == p4.x) and (p3.y == p4.y)


p3 = Point(3,4)
p4 = Point(3,4)	

same_coordinates( p3, p4 )







