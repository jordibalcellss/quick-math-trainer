# qmt

Quick math trainer: a command-line program written in Python.

## Description

When run with no parameters, the program runs a combo of 10 mixed questions (namely addition, subtraction, multiplication and/or division).

Specifying a number of operations (`-n/--number`) runs a set of questions. If either `-o/--operation` or `-d/--difficulty` are not specified, the set will be composed of the four operation types and up to 5 difficulties, both randomly chosen.

Once finished, the program prints stats about the exercise, comparing the average turnaround times of previous similar questions with those from the last exercise.

## Usage

```
$ qmt.py -h
usage: qmt.py [-h] [-c] [-n NUMBER] [-o {add,sub,mul,div}] [-d {1,2,3,4,5}]
```

## License

This project is licensed under the GNU General Public License - see the LICENSE file for details.













