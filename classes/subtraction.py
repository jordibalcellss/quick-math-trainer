from .operation import Operation
from random import randrange as randrange

class Subtraction(Operation):
    """Prepares a subtraction with two terms.

    Difficulty levels:

    1. terms up to 10
    2. terms between 11 and 99 and not multiple of 10
    3. terms between 101 and 999 and not multiple of 100
    4. terms between 1001 and 9999 and not multiple of 1000
    5. terms between 10001 and 99999 and not multiple of 10000
       but multiple of 10
    """

    def __init__(self, difficulty):
        self.operator = {'symbol': '—', 'code': 'sub'}
        self.difficulty = difficulty
        self.set_operands()

    def set_operands(self):
        """Calculates operands."""

        self.operands = []
        self.set_operands_by_difficulty()
        
        # Avoid negative results
        self.operands.sort(reverse=True)

        # Obtain the result for question()
        self.result = self.operands[0] - self.operands[1]
