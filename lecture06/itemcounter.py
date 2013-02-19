# Your goal is to make ItemCounter work with the sample code below.
# You can change ItemCounter as much as you'd like.
# Consider using __getitem__ or __setitem__ functions to make ItemCounter
# behave like a dictionary.
# See: http://docs.python.org/2/reference/datamodel.html#object.__getitem__
# See: http://docs.python.org/2/reference/datamodel.html#object.__setitem__

# You should write this code
class ItemCounter:
    pass

# Some sample code for you
counter = ItemCounter()
for x in [1, 2, 3, 3, 3, 5, 6]:
    counter[x] += 1
print "There are %d 3's in the list" % counter[3]
