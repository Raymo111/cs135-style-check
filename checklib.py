class Checker:
	def __init__(self, code=None, DEBUG=None):
		self.DEBUG = DEBUG
		self.code = code

	def check(self):
		code = self.code
		for i, line in enumerate(code):
			if i > 3:
				print(line, end='')
