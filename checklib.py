import re

import Strings

DEBUG = None
warncount = 0
errcount = 0
functionIdentifiers = []


class Checker:
	def __init__(self, code=None):
		self.code = code

	def check(self):
		w = Strings.StyleWarning
		e = Strings.StyleError
		code = self.code
		if not checkForConstant(code):
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
				warn(w.WHITESPACE, i)
			if checkComment(line):
				error(e.FULLLINECOMMENT, i)
			if checkConstLen(line):
				warn(w.CONSTLEN, i)
			if not checkConstUsage(code, line):
				error(e.CONSTNOTUSED, i)
			if i == len(code) and isBlank(code[i - 1]):
				error(e.LINEBLANK)
			if checkElseCond(line):
				error(e.ELSECOND)

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
	return not line or line in ['\n', '\r\n']


def isConstant(line):
	return line.startswith("(define ") and line[8] != '('


def getOccurrences(code, string):
	occ = []
	for i, line in enumerate(code):
		if string in line:
			occ.append(i)
	return occ


def fmtPrint(line):
	if DEBUG:
		prepend = "> "
	else:
		prepend = ""
	if line is not None:
		lineInfo = f" (line {line + (3 if DEBUG else 0)})"
	else:
		lineInfo = ""
	return [prepend, lineInfo]


# Check functions
# Check for 8-digit UWaterloo student number

def checkForConstant(code):
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
		return line.isspace() or tooManyTogether or commonIssue


# checks for design error of having cond in else bracket
def checkElseCond(line):
	elseCond = re.search(r"\[else \(cond", line)
	return elseCond


# Full-line comments should use 2 semicolons
def checkComment(line):
	if not isComment(line):
		return line.startswith(';')


# Constants shouldn't be <3 chars
def checkConstLen(line):
	if isConstant(line):
		return len(line.split()[1]) < 3


# Constants shouldn't be unused
def checkConstUsage(code, line):
	if isConstant(line):
		return len(getOccurrences(code, line.split()[1])) > 1
	return True


def checkPurposeExists(line):
	pass


def checkContractExists(line):
	pass


def checkExamplesExist(line):
	pass


def checkRequiresExist(line):
	pass
