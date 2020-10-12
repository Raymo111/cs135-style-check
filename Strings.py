class StyleWarning:
	CONSTLEN = "Constant too crpytic"
	LINENOTBLANK = "Should be blank"
	MISSINGCONSTANTS = "You don't have any constants"
	MISSINGREQ = "You don't have a Requires statement"


class StyleError:
	CONSTNOTUSED = "Unused constant"
	EOFNOTBLANK = "Missing blank last line"
	LINEBLANK = "Extra blank line"
	FILELABEL = "Missing Assignment/Problem number"
	FULLLINECOMMENT = "Full-line comments should start with 2 semicolons"
	LINETOOLONG = "Over 80 characters"
	STUDENTNUM = "Missing Student ID"
	WHITESPACE = "Whitespace issue"
