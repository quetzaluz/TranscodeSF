class JustZero:
    def num(self):
        return 0

    def print_num(self):
        print self.num()


class OneOneOne(JustZero):
    def num(self):
        return 111


class TwoTwoTwo(JustZero):
    def num(self):
        return 222


class TwoTwoTwoModified(TwoTwoTwo):
    def num(self, x):
        return x


class QuestionOne(OneOneOne, TwoTwoTwo):
    pass


class QuestionTwo(TwoTwoTwo, OneOneOne):
    pass


class QuestionThree(TwoTwoTwo, OneOneOne):
    def num(self):
        return 3


class QuestionFour(JustZero, TwoTwoTwo, OneOneOne):
    pass


class QuestionFive(TwoTwoTwoModified, OneOneOne):
    def print_num(self):
        print self.num(9)


if __name__ == '__main__':
    QuestionOne().print_num()
    QuestionTwo().print_num()
    QuestionThree().print_num()
    QuestionFour().print_num()
    QuestionFive().print_num()
