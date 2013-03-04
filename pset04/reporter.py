"""
Some more background hints:

As part of the in-class assignment on 2/19, you implemented your own
version of the Python Counter class.

See: http://docs.python.org/2/library/collections.html#collections.Counter

You overloaded the __getitem__ and __setitem__ functions to make a class
support the [] indexing operators to get and set key/value pairs, as if it
were a dictionary.

Python also allows you to override the __getattr__ funtion to allow you
to modify the way accessing attributes works for your class.  In other
words, if you have a class SomeClass, and you override __getattr__,
your __getattr__ function will get called any time somebody tries to
do something like:

    x = SomeClass()
    print x.some_attribute  # calls __getattr__

It doesn't matter that x may not even have such an attribute!
So, you could theoretically make some class that never has an
AttributeError and could pretend like it has any attribute you ever
ask for it.  That's easy.  ;)

It turns out that member functions in Python are really just stored as
attributes.  The attributes are just function objects.  So, if you want a class
that pretends like it has any function that you want to call on it, then you
just need to make a class where any attribute you access returns a function
that does what you want it to do.

If you need to remember more about Python functions as objects, read:
http://marakana.com/bookshelf/python_fundamentals_tutorial/functional_programming.html

It may be helpful to work towards this problem in stages:

Goal 0: Make the class pretend like it has every attribute, so that accessing
x.some_attribute just gives you the value "some_attribute" as a string.

Goal 1: Make the class just print out "You called a function" whenever you
call any function on it.

Goal 2: Make the class print out "You called function 'name'" with the name of the function, whenever you call a function on it.

Goal 3: Support variable numbers of arguments.  Remember:
http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
"""

class FunctionReporter:
    def __getattr__(self, name):
        strname = str(name)
        def name(*args):
            counter = 0
            dict1 = {-1: "You called the '%s' function." % strname}
            for arg in args:
                dict1[counter] = arg
                counter += 1
            for entry in dict1:
                if entry == -1:
                    print dict1[-1]
                else:
                    print "Arg %s: %s" % (str(entry), str(dict1[entry]))
        return name
        
            

if __name__ == '__main__':
    x = FunctionReporter()
    x.foo()
    x.anything()
    x.func_with_params(3, "x", True)
