import re

import Strings

global DEBUG


class Checker:
	def __init__(self, code=None):
		self.code = code

	def check(self):
		w = Strings.StyleWarning
		e = Strings.StyleError
		code = self.code
		for i, line in enumerate(code, 1):
			if DEBUG:
				print(line, end='')
			if len(line) > 80:
				error(i, e.LINETOOLONG)
			if i == 3 and not checkStudentNum(line):
				error(i, e.STUDENTNUM)
			if i == 5 and not checkFileLabel(line):
				error(i, e.FILELABEL)
			if i == 8 and not isBlank(line):
				warn(i, w.LINENOTBLANK)


# Output functions
def warn(line, warning):
	if DEBUG:
		prepend = "> "
	print(f"{prepend}Warning (line {line}): {warning}")


def error(line, error):
	if DEBUG:
		prepend = "> "
	print(f"{prepend}Error (line {line}): {error}")


# Helper functions
def isComment(line):
	return line.startswith(';;')


def isBlank(line):
	return line in ['\n', '\r\n']


# Check functions
# Check for 8-digit UWaterloo student number
def checkStudentNum(line):
	res = re.search(r"\(\d{8}\)", line)
	return res and isComment(line)


# Check for Assignment/Problem number
def checkFileLabel(line):
	res = re.search(r"Assignment \d+, Problem \d+", line)
	return res and isComment(line)
