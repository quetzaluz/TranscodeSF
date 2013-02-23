# Your goal is to make ItemCounter work with the sample code below.
# You can change ItemCounter as much as you'd like.
# Consider using __getitem__ or __setitem__ functions to make ItemCounter
# behave like a dictionary.
# See: http://docs.python.org/2/reference/datamodel.html#object.__getitem__
# See: http://docs.python.org/2/reference/datamodel.html#object.__setitem__

# One way to implement this using has-a
class ItemCounterHasA(object):
    def __init__(self):
        self._d = {}

    def __getitem__(self, key):
        if key in self._d:
            return self._d[key]
        return 0

    def __setitem__(self, key, value):
        self._d[key] = value

# Another way to implement this using is-a
class ItemCounterIsA(dict):
    def __getitem__(self, key):
        if key in self:
            return super(self, ItemCounter).__getitem__(self, key)
        return 0

# Set ItemCounter to be one of the above classes.
ItemCounter = ItemCounterHasA
# ItemCounter = ItemCounterIsA

# Some sample code for you
counter = ItemCounter()
for x in [1, 2, 3, 3, 3, 5, 6]:
    counter[x] += 1
print "There are %d 3's in the list" % counter[3]
