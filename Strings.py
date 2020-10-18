class StyleWarning:
	CONSTLEN = "Constant too crpytic"
	LINENOTBLANK = "Should be blank"
	MISSINGCONSTANTS = "You don't have any constants"
	MISSINGREQ = "You don't have a Requires statement"
	WHITESPACE = "Whitespace issue"


class StyleError:
	CONSTNOTUSED = "Unused constant"
	ELSECOND = "Else should not have conditionals inside"
	EOFNOTBLANK = "Missing blank last line"
	FILELABEL = "Missing Assignment/Problem number"
	FULLLINECOMMENT = "Full-line comments should start with 2 semicolons"
	LINEBLANK = "Extra blank line"
	LINETOOLONG = "Over 80 characters"
	MISSINGEOF = "You don't have an empty last line"
	STUDENTNUM = "Missing Student ID"
