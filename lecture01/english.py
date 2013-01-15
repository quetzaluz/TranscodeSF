def englishify(num):
    """ This function takes an integer and returns a string representing
    the written out English version.  For instance,

        2 => "two"
        34 => "thirty-four"
        509 => "five hundred nine" (alternatively, "five hundred and nine")

    See http://www.eslcafe.com/grammar/saying_large_numbers01.html for more
    examples.
    """

    # Insert your code here.
    return str(num)

if __name__ == '__main__':
    test = [3, 34, 509, 0, 12]
    for num in test:
        print "%d => %s" % (num, englishify(num))
