import os.path

class History:
    """Manages user's history and provides stats."""

    def __init__(self):
        pass

    def clear():
        """Removes ~/.qmt-history"""

        if os.path.exists(os.path.expanduser('~') + '/.qmt-history'):
            os.remove(os.path.expanduser('~') + '/.qmt-history')

    def save(self, history):
        """Writes Operation.history into the history file"""

        with open(os.path.expanduser('~') + '/.qmt-history', 'a') as f:
            for line in history:
                f.write(f'{line}\n')

    def stats(self, history):
        """Computes the average resolution times for unique pairs of operations
        (difficulty and operator). The comparisons are provided for operations
        that came up in the last execution and can be paired to meaningful
        historic values.

        The reason behind comparing unique pairs and not operations with the
        same difficulty regardless of the operator is that the difficulty
        levels are arbitrary and might not require the same mental load across
        different types of operations.
        """

        self.save(history)

        print()

        pairs = []
        for operation in history:
            pairs.append(operation.split()[0])
        # Get unique values
        pairs = list(set(pairs))
        pairs.sort()

        # Loop the history sequence (last run)
        time_avg_last = []
        for pair in pairs:
            time, count = 0, 0
            for operation in history:
                if operation.split()[0] == pair:
                    time = time + float(operation.split()[3])
                    count = count + 1
            time_avg_last.append(time / count)

        # Print column headers
        print('{:<11} {} {:>6}'.format('d-ope', 'hist', 'last'))

        # Read the history file and print stats
        i = 0
        for pair in pairs:
            time, count = 0, 0
            with open(os.path.expanduser('~') + '/.qmt-history', 'r') as f:
                for operation in f:
                    if operation.split()[0] == pair:
                        time = time + float(operation.split()[3])
                        count = count + 1
                time_avg = time / count
                time_avg_last_r = round(time_avg_last[i] / time_avg, 1)
                if time_avg_last_r < 1:
                    time_avg_last_r = '\033[32m{}x\033[0m'.format(
                        round(1 / time_avg_last_r, 1))
                    trend = '\033[32mspeedup\033[0m'
                elif time_avg_last_r > 1:
                    time_avg_last_r = '\033[90m{}x\033[0m'.format(
                        time_avg_last_r)
                    trend = '\033[90mavg\033[0m'
                else:
                    time_avg_last_r = ''
                    trend = ''
                print('{:<9} {:>5}s {:>5}s {:>5} {}'.format(
                    pair,
                    round(time_avg, 1),
                    round(time_avg_last[i], 1),
                    time_avg_last_r,
                    trend))
                i = i + 1
