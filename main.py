import argparse
import sys

import checklib

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Check the style of a racket file')
	parser.add_argument('file', help='.rkt file to check style for')
	parser.add_argument('-d', "--debug", help="Output go brrrrrrrrrrrrr", action="store_true")
	args = parser.parse_args()

	try:
		if args.debug:
			print("In debug mode: output will go brrrrrrrrrrrrr")
			checklib.DEBUG = args.debug
		else:
			sys.tracebacklimit = 0
		with open(args.file) as file:
			code = file.read().splitlines(True)
			checker = checklib.Checker(code[3:])  # Lines 0,1,2 are autoinserted by DrRacket
			checker.check()
	except KeyboardInterrupt:
		print("\nBYE!")
		exit()
