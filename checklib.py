import re
import Strings


def warn(line, warning):
	print(f"Warning (line {line}): {warning}")


def error(line, error):
	print(f"Error (line {line}): {error}")


class Checker:
	def __init__(self, code=None, debug=None):
		self.DEBUG = debug
		self.code = code

	def check(self):
		w = Strings.StyleWarning
		e = Strings.StyleError
		code = self.code
		for i, line in enumerate(code):
			n = i - 3
			if n == 2 and not checkStudentNum(line):
				error(n, e.STUDENTNUM)

def checkStudentNum(line):
	res = re.search(r"\(\d{8}\)", line)
	if not res:
		return False
	return True