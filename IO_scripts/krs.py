#! /bin/python
# Krishna --- try writing and reading a file
# need to use this on ESXi

import sys, getopt
import random
#from __future__ import print_function

# set a pattern
# open a file --- write the pattern to it  multiple times --- close file
# save the number of times
# open same file --- read the contents for the same number of times ---- close the file


def debugPrint(str="", value=""):
        print "DEBUG:   ", str, value;

def printLine(lines=1):
   while lines > 0:
        print "--------------------------------------------------"
        lines = lines - 1
        print "";


Multiplier = 1048576

# create a pattern -- mark its length -- chose a random number of iterations to write
str="1234567890abcdefghijklmnop\3894729"
lenOfStr = len(str)
iterations=random.randrange(1, 10, 2) * Multiplier
debugPrint ("Length of str= ", lenOfStr)
debugPrint ("Iterations= ", iterations)
expectedSize = iterations * lenOfStr
debugPrint ("Expected size of file= ", expectedSize)
printLine()


# open a file -- write the pattern for the chosen number of iterations -- close file
file="/scratch/esxOndisk"
fd = open(file, "wb")
if (fd == 0) :
        print "Could not open file for writing"
        sys.exit();
i=0
while (i < iterations):
        fd.write(str)
        i = i+1
fd.close()

# --- chose a random point to start from (as a multiple of the len of str)
starter=random.randrange(0, iterations, 1)
debugPrint ("starting point is ", starter)
starter = starter * lenOfStr
debugPrint ("starting point as a multiple of string length = ", starter)
printLine()

# open same file
# position the pointer of the file at that point --- and read exactly the len of str
# close file

fd2 = open(file, "rb")
if (fd2 == 0) :
        print "Could not open file for reading"
        exit();
fd2.seek(starter,0)
debugPrint ("Location in file is now ", fd2.tell())
outstr = fd2.read(lenOfStr)
fd2.close()

# compare the output string and the original string
debugPrint ("Output string: ", outstr)
printLine(5)

if (outstr != str) :
        print "ERROR!!! ", starter, outstr, expectedSize
else :
        print "Success! ", starter, expectedSize

#!!!!!!!!Krishna
exit();

