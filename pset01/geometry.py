import numbers
    #### This is a work in progress!!! ####
class  Box:
    def __init__(self, x, y, width, height):
    # The try/except below ensures that only integer values are used.  
        parsedx = False
        parsedy = False
        parsedwid = False
        parsedhei = False
        poswid = False
        poshei = False
        while parsedx == False:
            try:
                self.x = int(x)
                parsedx = True
            except ValueError:
                print "Invalid value for x!"
                x = raw_input("Please enter an integer for x:")
            else:
                break
        while parsedy == False:
            try:
                self.y = int(y)
                parsedy = True
            except ValueError:
                print "Invalid value for y!"
                y = raw_input("Please enter an integer for y:")
        while parsedwid == False:
            try:
                self.width = int(width)
                parsedwid = True
            except ValueError:
                print "Invalid value for width!"
                width = raw_input("Please enter a positive integer for width:")
        while parsedhei == False:
            try:
                self.height = int(height)
                parsedhei = True
            except ValueError:
                print "Invalid value for height!"
                height = raw_input("Please enter a positive integer for height:")
        if width >= 0:
            pass
        else:
            print "Width must be a positive value! Converting to a positive value..."
            width = width * -1
            print "Width value was -" + str(width) + ", now it is " + str(width) + '.'
            pass
        if height >= 0:
            pass
        else:
            print "Height must be a positive value! Converting to a positive value..."
            height = height * -1
            print "Width value was -" + str(height) + ", now it is " + str(height) + "."
            pass
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
