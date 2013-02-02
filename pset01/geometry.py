class  Box:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        try:
            self.width = width
            self.height = height
            if self.width < 0:
                raise ValueError, "No such thing as a negative width value! Try again."
            if self.height < 0:
                raise ValueError, "No such thing as a negative height value! Try again."
        finally:
            print "Box " + str(self) + " created."
    def top(self):
        return self.y
    def bottom(self):
        return self.y + self.height
    def left(self):
        return self.x
    def right(self):
        return self.x + self.width
    def area(self):
        return self.width*self.height
    def __str__(self):
        return "(%s, %s) => (%s, %s)" % (self.left(), self.top(), self.right(), self.bottom())
    def is_intersecting(self, other):
        if self.left() > other.left() and self.left() < other.right():
            return True
        if self.right() > other.left() and self.right() < other.right():
            return True
        if self.top() > other.top() and self.top < other.bottom():
            return True
        if self.bottom() > other.top() and self.bottom < other.bottom():
            return True
        else:
            return False
        
    def intersect(self, other):
        if self.is_intersecting(other) == True:
            if self.left() < other.left():
                self.width = self.width - (other.x - self.x)
                self.x = other.x
            if self.top() < other.top():
                self.height = self.height - (other.y - self.y)
                self.y = other.y
            if self.right() > other.right():
                self.width = other.width - (self.x - other.x)
                if self.width < 0:
                    self.width = 0
            if self.bottom() > other.bottom():
                self.height = other.height - (self.y - other.y)
                if self.height < 0:
                    self.height = 0
        else:
            print "******************************************************"
            print "*            These boxes do not intersect!           *"
            print "*    Would you like to set box1(x, y) to box2(x,y)   *"
            print "*     and set the height and width of box1 to 0?     *"
            print "******************************************************"
            confirm = 0
            while confirm != 'y' or confirm != 'n':
                confirm = str(raw_input("Enter 'y' to set new coordinates, enter 'n' to abort:"))
                if confirm == 'y':
                    self.x = other.x
                    self.y = other.y
                    self.width = 0
                    self.height = 0
                    print "Box modified to become " + str(self) +". This"
                    print "point intersects with box " + str(other) +"."
                    break
                if confirm == 'n':
                    print "Box " + str(self) + " is unchanged. This box"
                    print "doesn't intersect with box " + str(other) + "."
                    break
print ">>> b = Box(2, 3, 8, 4)"
b = Box(2, 3, 8, 4)
print ">>> b1 = Box(0, 0, 10, 10)b = Box(2, 3, 8, 4)"
b1 = Box(0, 0, 10, 10)
print ">>> b2 = Box(2, 3, 20, 6)"
b2 = Box(2, 3, 20, 6)
print ">>> b3 = Box(10, 12, 3, 4)"
b3 = Box(10, 12, 3, 4)
print ">>> b.left()"
print b.left()
print ">>> b.right()"
print b.right()
print ">>> b.top()"
print b.top()
print ">>> b.bottom()"
print b.bottom()
print ">>> print b"
print b
print ">>> b.area()"
print b.area()
print ">>> b1 = Box(0, 0, 10, 10)"
b1 = Box(0, 0, 10, 10)
print ">>> b2 = Box(10, 4, 2, 3)"
b2 = Box(10, 4, 2, 3)
print ">>> b3 = Box(-5, 5, 7, 3)"
b3 = Box(-5, 5, 7, 3)
print ">>> empty = Box(5, 5, 0, 0)"
empty = Box(5, 5, 0, 0)
print ">>> b1.is_intersecting(b2)"
print b1.is_intersecting(b2)  # adjacent boxes are not intersecting
print ">>> b2.is_intersecting(b3)"
print b2.is_intersecting(b3)
print ">>> b1.is_intersecting(b3)"
print b1.is_intersecting(b3)
print ">>> b1.is_intersecting(empty)"
print b1.is_intersecting(empty)  # empty boxes don't intersect anything
print ">>> b1 = Box(0, 0, 10, 10)"
b1 = Box(0, 0, 10, 10)
print ">>> b2 = Box(2, 3, 20, 6)"
b2 = Box(2, 3, 20, 6)
print ">>> b3 = Box(10, 12, 3, 4)"
b3 = Box(10, 12, 3, 4)
print ">>> b1.intersect(b2)"
b1.intersect(b2)
print ">>> print b1"
print b1
print ">>> print b2"
print b2  # b2 is unchanged
print ">>> b2.intersect(b3)"
b2.intersect(b3)
print ">>> b2.area()"
print b2.area()  # The x,y location of b2 are not important
print "******************************************************"
print "*    Optional: try creating a box with a negative    *"
print "*    height or width value. An error will result.    *"
print "******************************************************"
