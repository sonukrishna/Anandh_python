"""create a pattern using class """

class Canvas:
    def __init__(self,width,height):
	self.width=width
	self.height=height
	self.data=[[' ']*width for i in range(height)]
    def setpixel(self,row,column):
	self.data[row][column]='*'
    def getpixel(self,row,column):
	return self.data[row][column]
    def display(self):
	print "\n".join(["".join(row) for row in self.data])

class Shape:
    def paint(self,canvas):
	pass
class Rectangle(Shape):
    def __init__(self,x,y,w,h):
	self.x=x
	self.y=y
	se	

aa=Canvas(2,3)
aa.display()

