from .operation import Operation
from random import randrange as randrange
from random import shuffle as shuffle

class Multiplication(Operation):
    """Prepares a multiplication with two factors.

    Difficulty levels:

    1. factors between 2 and 9
    2. one factor between 2 and 9, the other a multiple of 10 up to 100
    3. factors between 11 and 99 where one factor is a multiple of 10
    4. one factor between 101 and 999, the other up to 9
    5. factors between 11 and 99 with no multiples of 10
    """

    def __init__(self, difficulty):
        self.operator = {'symbol': '×', 'code': 'mul'}
        self.difficulty = difficulty
        self.set_operands()

    def set_operands(self):
        """Calculates operands according to difficulty."""

        self.operands = []
        if self.difficulty == 1:
            self.operands = [randrange(2, 10), randrange(2, 10)]
        elif self.difficulty == 2:
            self.operands = [randrange(2, 10), randrange(10, 101, 10)]
            shuffle(self.operands)
        elif self.difficulty == 3:
            self.operands = [randrange(11, 100), randrange(20, 100, 10)]
            shuffle(self.operands)
        elif self.difficulty == 4:
            self.operands = [randrange(101, 1000), randrange(2, 10)]
            shuffle(self.operands)
        elif self.difficulty == 5:
            i = 0
            while i < 2:
                operand = randrange(11, 100)
                if operand % 10 != 0:
                    self.operands.append(operand)
                    i = i + 1

        # Obtain the result for question()
        self.result = self.operands[0] * self.operands[1]
