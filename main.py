import sys

import checklib
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Check the style of a racket file')
	parser.add_argument('file', help='.rkt file to check style for')
	parser.add_argument('-d', "--debug", help="Output go brrrrrrrrrrrrr", action="store_true")
	args = parser.parse_args()

	try:
		if args.debug:
			print("In debug mode: output will go brrrrrrrrrrrr")
		else:
			sys.tracebacklimit = 0
		with open(args.file) as file:
			checker = checklib.Checker(file, args.debug)
			checker.check()
	except KeyboardInterrupt:
		print("\nBYE!")
		exit()
