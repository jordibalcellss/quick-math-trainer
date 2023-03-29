from .operation import Operation
from random import randrange as randrange, getrandbits as getrandbits
from random import shuffle as shuffle

class Division(Operation):
    """Prepares an integer division.

    Difficulty levels:

    1. both dividend and divisor with a single digit
    2. dividend up to 81, divisor up to 9
    3. 3-digit dividend, single digit divisor
    4. 4-digit dividend, single digit divisor, or
       3-digit dividend, 2-digit divisor
    5. 4-digit dividend, 2-digit divisor
    """

    def __init__(self, difficulty):
        self.operator = {'symbol': '/', 'code': 'div'}
        self.difficulty = difficulty
        self.set_operands()

    def set_operands(self):
        """Calculates operands according to difficulty."""

        self.operands = []
        if self.difficulty == 1:
            self.find_a_divisor(2, 10)
        if self.difficulty == 2:
            factors = [randrange(2, 10), randrange(2, 10)]
            self.operands.append(factors[0] * factors[1])
            shuffle(factors)
            self.operands.append(factors[0])
        if self.difficulty == 3:
            self.find_a_divisor(100, 1000, 2, 10)
        if self.difficulty == 4:
            choice = bool(getrandbits(1))
            if choice:
                self.find_a_divisor(1000, 10000, 2, 10)
            else:
                self.find_a_divisor(100, 1000, 11, 100)
        if self.difficulty == 5:
            self.find_a_divisor(1000, 10000, 11, 100)

        # Obtain the result for question()
        self.result = self.operands[0] / self.operands[1]

    def find_a_divisor(self, dd_start, dd_stop, ds_start='', ds_stop=''):
        """Finds a divisor for a random dividend. The dividend range is
        defined by the the dd_ arguments (mandatory), the divisor one by the
        ds_ arguments (optional)
        """

        # ds_ equals to dd_ if not passed
        if not len(str(ds_start)):
            ds_start = dd_start
        if not len(str(ds_stop)):
            ds_stop = dd_stop

        # We'll loop over an scrambled list of divisor candidates
        divisors = list(range(ds_start, ds_stop))
        shuffle(divisors)

        not_found = True
        while not_found:
            dividend = randrange(dd_start, dd_stop)
            if not self.is_prime(dividend):
                for divisor in divisors:
                    if dividend % divisor == 0:
                        # A divisor was found, let's pack up
                        self.operands.append(dividend)
                        self.operands.append(divisor)
                        not_found = False
                        break

    def is_prime(self, num):
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False
