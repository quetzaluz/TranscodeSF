# Your goal is to make ItemCounter work with the sample code below.
# You can change ItemCounter as much as you'd like.
# Consider using __getitem__ or __setitem__ functions to make ItemCounter
# behave like a dictionary.
# See: http://docs.python.org/2/reference/datamodel.html#object.__getitem__
# See: http://docs.python.org/2/reference/datamodel.html#object.__setitem__

# You should write this code

# __getitem_ x[key] (self,key)
# __setitem__ is like x[key] = value (self,key,value)

"""
class ItemCounter(object):
        def __init__(self):
                dict = {}
        def __getitem__(self, key):
                dict.append(key[)
        def __setitem__(self, key, value):
                if key == value:
                        
                        

                

# Some sample code for you
counter = ItemCounter()
for x in [1, 2, 3, 3, 3, 5, 6]:
        counter[x] += 1
print "There are %d 3's in the list" % counter[3]



"""


##Teacher solution:
class ItemCounter(object):
        def __init__(self):
                self._d = {}
        def __getitem__(self, key):
                if key in self._d:
                        return self._d[key]
                # at this point you can append the key, or you can...
                return 0
        def __setitem__(self, key, value):
                self._d[key] = value

counter = ItemCounter()
for x in [1, 2, 3, 3, 3, 5, 6]:
        counter[x] += 1
print "There are %d 3's in the list" % counter[3]

# OUTPUT:
#There are 3 3's in the list
#>> print counter._d
#{1: 1, 2: 1, 3: 3, 5: 1, 6: 1}

# Alternative solution with ItemCounter is-a dictionary rather than has-a dictionary

class ItemCounter(dict):
        def __getitem__(self, key):
                if key in self:
                        return dict.__getitem__(self, key) #dict called to overide definition above
                        #alternative: return super(self, ItemCounter).__getitem__(self, key) Good if you change what you're deriving from.
                return 0
