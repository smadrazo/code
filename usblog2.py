#!/usr/bin/env python

import sys

logFile = open(sys.argv[1])
print "Printing all lines with USB in it ..."

for line in logFile.readlines():
    if line.lower().find("usb") != -1:
        print line

print "Done!"
