import re

import Strings

DEBUG = None
warncount = 0
errcount = 0


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
		if warncount == 0 and errcount == 0:
			print("All good! No errors or warnings.")
		elif errcount == 0:
			print(f"Total {warncount} warnings and no errors. Double-check your code!")
		else:
			print(f"Total {errcount} errors and {'no' if warncount == 0 else warncount} warnings. Fix up your code!")


# Output functions
def warn(line, warning):
	if DEBUG:
		prepend = "> "
	print(f"{prepend}Warning (line {line}): {warning}")
	global warncount
	warncount += 1


def error(line, err):
	if DEBUG:
		prepend = "> "
	print(f"{prepend}Error (line {line}): {err}")
	global errcount
	errcount += 1


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
