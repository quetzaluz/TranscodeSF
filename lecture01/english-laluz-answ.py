def englishify(num):
    """ This function takes an integer and returns a string representing
    the written out English version.  For instance,

        2 => "two"
        34 => "thirty-four"
        509 => "five hundred nine" (alternatively, "five hundred and nine")

    See http://www.eslcafe.com/grammar/saying_large_numbers01.html for more
    examples.
    """

    # NOTE: This solution will probably horrify anyone who can
    # more competently code. Relies on a lot of if statements,
    # works with the list provided in the example, but glitches
    # when handling negative numbers.

    lis = []
    ones = ""
    tens = ""
    hund = ""
    thou = ""
    comm = ""
    and1 = ""
    hyph = ""
    numlength=len(str(num))
    while numlength != 0:
        x = num % 10
        lis.append(x)
        num = (num - x)/10
        numlength -= 1
    if len(lis) == 1:
        if lis[0] == 0:
            ones = "zero"
        if lis[0] == 1:
            ones = "one"
        if lis[0] == 2:
            ones = "two"
        if lis[0] == 3:
            ones = "three"
        if lis[0] == 4:
            ones = "four"
        if lis[0] == 5:
            ones = "five"
        if lis[0] == 6:
            ones = "six"
        if lis[0] == 7:
            ones = "seven"
        if lis[0] == 8:
            ones = "eight"
        if lis[0] == 9:
            ones = "nine"
    if len(lis) > 1:
        if lis[1] == 1 and lis[0] == 1:
            tens = "eleven"
        if lis[1] == 1 and lis[0] == 2:
            tens = "twelve"
        if lis[1] == 1 and lis[0] == 3:
            tens = "thirteen"
        if lis[1] == 1 and lis[0] == 4:
            tens = "fourteen"
        if lis[1] == 1 and lis[0] == 5:
            tens = "fifteen"
        if lis[1] == 1 and lis[0] == 6:
            tens = "sixteen"
        if lis[1] == 1 and lis[0] == 7:
            tens = "seventeen"
        if lis[1] == 1 and lis[0] == 8:
            tens = "eighteen"
        if lis[1] == 1 and lis[0] == 9:
            tens = "nineteen"
        if lis[1] == 1 and lis[0] == 0:
            tens = "ten"
        if lis[1] == 2:
            tens = "twenty"
        if lis[1] == 3:
            tens = "thirty"
        if lis[1] == 4:
            tens = "forty"
        if lis[1] == 5:
            tens = "fifty"
        if lis[1] == 6:
            tens = "sixty"
        if lis[1] == 7:
            tens = "seventy"
        if lis[1] == 8:
            tens = "eighty"
        if lis[1] == 9:
            tens = "ninety"
        if lis[1] != 1 and lis[0] == 1:
            ones = "one"
        if lis[1] != 1 and lis[0] == 2:
            ones = "two"
        if lis[1] != 1 and lis[0] == 3:
            ones = "three"
        if lis[1] != 1 and lis[0] == 4:
            ones = "four"
        if lis[1] != 1 and lis[0] == 5:
            ones = "five"
        if lis[1] != 1 and lis[0] == 6:
            ones = "six"
        if lis[1] != 1 and lis[0] == 7:
            ones = "seven"
        if lis[1] != 1 and lis[0] == 8:
            ones = "eight"
        if lis[1] != 1 and lis[0] == 9:
            ones = "nine"
        if lis[1] > 1 and lis[0] >= 1:
            hyph = "-"
    if len(lis) > 2:
        if lis[2] == 1:
            hund = "one hundred"
        if lis[2] == 2:
            hund = "two hundred"
        if lis[2] == 3:
            hund = "three hundred"
        if lis[2] == 4:
            hund = "four hundred"
        if lis[2] == 5:
            hund = "five hundred"
        if lis[2] == 6:
            hund = "six hundred"
        if lis[2] == 7:
            hund = "seven hundred"
        if lis[2] == 8:
            hund = "eight hundred"
        if lis[2] == 9:
            hund = "nine hundred"
        if lis[2] > 0 and lis[1] != 0 or lis [0] != 0:
            and1 = " and "
    if len(lis) > 3:
        if lis[3] == 1:
            thou = "one thousand"
        if lis[3] == 2:
            thou = "two thousand"
        if lis[3] == 3:
            thou = "three thousand"
        if lis[3] == 4:
            thou = "four thousand"
        if lis[3] == 5:
            thou = "five thousand"
        if lis[3] == 6:
            thou = "six thousand"
        if lis[3] == 7:
            thou = "seven thousand"
        if lis[3] == 8:
            thou = "eight thousand"
        if lis[3] == 9:
            thou = "nine thousand"
        if lis[3] >=1 and lis[2] == 0 and lis[1] !=0:
            comm = ""
            and1 = " and "
        elif lis[3] >=1 and lis[2] == 0 and lis[1] == 0 and lis[0] !=0:
            comm = ""
            and1 = " and "
        elif lis[3] >=1 and lis[2] !=0 and lis[1] != 0 and lis[0] !=0:
            comm = ", "
            and1 = " and "
        elif lis[3] >= 1 and lis[2] !=0 and lis[1] == 0 and lis[0] !=0:
            comm = ", "
            and1 = " and "
        elif lis[3] >= 1 and lis[2] !=0 and lis[1] == 0 and lis[0] ==0:
            comm = ", "
            and1 = ""
    num_word = thou + comm + hund + and1 + tens + hyph + ones
        
    return str(num_word)

if __name__ == '__main__':
    test = [3, 34, 509, 0, 12, 2009, 2013, 9999]
    for num in test:
        print "%d => %s" % (num, englishify(num))

