from time import perf_counter as timer
from random import randrange as randrange

class Operation:
    """Shared attributes and methods across operation types."""

    history = []

    def color(self, color, text):
        """Color an string"""

        text_color = f'\033[{color}{text}\033[00m'
        return text_color


    def question(self):
        """Prints out the question and waits for input.
        Counts the time elapsed until a correct answer comes in.
        Appends the operation in to history.
        """

        start = timer()
        while True:
            try:
                operation = (self.color('33m', str(self.operands[0]))
                    + ' ' + self.operator['symbol'] + ' ' +
                    self.color('33m', str(self.operands[1])))
                result = int(input(operation + ' = '))
                if result == self.result:
                    end = timer()
                    # The operations are stored in a sequence until the results
                    # are written to the history file once the main program
                    # loop finishes. The format is
                    # {difficulty-operator, operand, operand, time}
                    self.history.append('{}-{} {} {} {}'.format(
                        self.difficulty,
                        self.operator['code'],
                        self.operands[0],
                        self.operands[1],
                        round((end - start), 1)))
                    break
            except ValueError:
                pass

    def set_operands_by_difficulty(self):
        """
        Calculates operands according to difficulty (addition and subtraction).

        Discards multiples of powers of 10 proportionally to the number of
        digits. I. e., a summand of 4 digits will not be a multiple of 1000
        (10^(num_digits-1)).

        A term of 5 digits will always be a multiple of 10.

        Avoids zero result when subtracting.
        """

        # The number of digits corresponds to the difficulty
        start = 10 ** (self.difficulty - 1)
        stop = 10 ** self.difficulty

        while True:
            if self.difficulty == 5:
                operand = randrange(start, stop, 10)
            else:
                operand = randrange(start, stop)

            if (operand % 10 ** (self.difficulty - 1) != 0 or self.difficulty
                == 1):
                if len(self.operands):
                    # Force them differ when subtracting
                    if self.operator['code'] == 'sub':
                        if self.operands[0] != operand:
                            self.operands.append(operand)
                            break
                    else:
                        self.operands.append(operand)
                        break
                else:
                    self.operands.append(operand)
