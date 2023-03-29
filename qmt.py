#!/usr/bin/env python3

# quick-math-trainer
#
# Copyright 2023 by Jordi Balcells <jordi@balcells.io>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with 
# this program.
#
# If not, see <https://www.gnu.org/licenses/>.

import sys, argparse, textwrap

def int_positive(x):
    x = int(x)
    if x <= 0:
        raise argparse.ArgumentTypeError(
            "The number has to be a positive integer")
    return x

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
        Quick math trainer

        When run with no parameters, the program runs a combo
        of 10 mixed questions (namely addition, subtraction,
        multiplication and/or division).

        Specifying a number of operations (-n/--number) runs
        a set of questions. If either -o/--operation or
        -d/--difficulty are not specified, the set will be
        composed of the four operation types and up to 5
        difficulties, both randomly chosen.

        Once finished, the program prints stats about the
        exercise, comparing the average turnaround times of
        previous similar questions with those from the last
        exercise.
        '''))
parser.add_argument(
    '-c', '--clear-history',
    action='store_true',
    help='removes the history file')
parser.add_argument(
    '-n', '--number',
    type=int_positive,
    default=10,
    help='number of operations')
parser.add_argument(
    '-o', '--operation',
    choices = ['add', 'sub', 'mul', 'div'])
parser.add_argument(
    '-d', '--difficulty',
    type=int,
    choices=range(1, 6))
args = parser.parse_args()

if args.clear_history:
    from classes.history import History
    History.clear()
    sys.exit()

from classes.addition import Addition
from classes.subtraction import Subtraction
from classes.multiplication import Multiplication
from classes.division import Division
from random import randrange as randrange

def select_operation(difficulty, operation=''):
    """Instantiates and prints an operation"""
    
    if not len(operation):
        operations = ['add', 'sub', 'mul', 'div']
        operation = operations[randrange(0, 4)]
    if operation == 'add':
        o = Addition(difficulty)
    elif operation == 'sub':
        o = Subtraction(difficulty)
    elif operation == 'mul':
        o = Multiplication(difficulty)
    else:
        o = Division(difficulty)
    o.question()

if len(sys.argv) == 1:
    # Run a combo of 10 mixed operations
    # with increasing difficulty
    difficulties = [1, 2, 2, 3, 3, 3, 3, 4, 4, 5]
    for difficulty in difficulties:
        select_operation(difficulty)
else:
    # Provide a set according to parameters
    for i in range(args.number):
        if args.difficulty is None:
            difficulty = randrange(1, 6)
        else:
            difficulty = args.difficulty
        if args.operation is None:
            select_operation(difficulty)
        else:
            select_operation(difficulty, args.operation)

from classes.operation import Operation
from classes.history import History
o = Operation()
h = History()

# Print stats
h.stats(o.history)
