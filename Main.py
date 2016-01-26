#!/usr/bin/python

import sys

from Find_Files import Find_Files

if __name__ == "__main__":
	print "Running TransDecoder on all "+sys.argv[1]+" files in current working directory"
	print ""
	ff = Find_Files(sys.argv[1])
