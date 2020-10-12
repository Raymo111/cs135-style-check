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
		if not checkConstant(code):
			warn(w.MISSINGCONSTANTS)
		for i, line in enumerate(code, 1):
			# if DEBUG:
			# 	print(line, end='')
			if len(line) > 80:
				error(e.LINETOOLONG, i)
			if i == 3 and not checkStudentNum(line):
				error(e.STUDENTNUM, i)
			if i == 5 and not checkFileLabel(line):
				error(e.FILELABEL, i)
			if i == 8 and not isBlank(line):
				warn(w.LINENOTBLANK, i)
			if checkWhitespace(line):
				error(e.WHITESPACE, i)
		if warncount == 0 and errcount == 0:
			print("All good! No errors or warnings.")
		elif errcount == 0:
			print(f"Total {warncount} warnings and no errors. Double-check your code!")
		else:
			print(f"Total {errcount} errors and {'no' if warncount == 0 else warncount} warnings. Fix up your code!")


# Output functions
def warn(warning, line=None):
	fmt = fmtPrint(line)
	print(f"{fmt[0]}Warning{fmt[1]}: {warning}")
	global warncount
	warncount += 1


def error(err, line=None):
	fmt = fmtPrint(line)
	print(f"{fmt[0]}Error{fmt[1]}: {err}")
	global errcount
	errcount += 1


# Helper functions
def isComment(line):
	return line.startswith(';;')


def isBlank(line):
	return line in ['\n', '\r\n']


def fmtPrint(line):
	if DEBUG:
		prepend = "> "
	else:
		prepend = ''
	if line is not None:
		lineInfo = f" (line {line + 3 if DEBUG else 0})"
	else:
		lineInfo = ''
	return [prepend, lineInfo]


# Check functions
# Check for 8-digit UWaterloo student number
def checkConstant(code):
	for i, line in enumerate(code):
		if line.startswith("(define ("):
			if DEBUG:
				print(f"First function at line {i + 4}")
			for j in range(i - 1, 1, -1):
				if code[j].startswith("(define "):
					return True
			return False


def checkStudentNum(line):
	res = re.search(r"\(\d{8}\)", line)
	return res and isComment(line)


# Check for Assignment/Problem number
def checkFileLabel(line):
	res = re.search(r"Assignment \d+, Problem \d+", line)
	return res and isComment(line)


def checkWhitespace(line):
	tooManyTogether = re.match(r"(\S[ \f\t\v]{2,})", line)
	atEOL = re.match(r"[ \f\t\v]+$", line)
	afterOpenBracket = re.search(r"\([ \f\t\v]+", line)
	beforeCloseBracket = re.search(r"[ \f\t\v]+\)", line)
	beforeComma = re.search(r"[ \f\t\v]+,", line)
	noneAfterComma = re.search(r",\S", line)
	commonIssue = atEOL or afterOpenBracket or beforeCloseBracket or beforeComma or noneAfterComma
	if isBlank(line):
		return False
	elif isComment(line):
		return commonIssue
	else:
		return tooManyTogether or commonIssue
