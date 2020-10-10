class Checker:
	def __init__(self, code=None, DEBUG=None):
		self.DEBUG = DEBUG
		self.code = code

	def check(self):
		code = self.code
		print(code.read())