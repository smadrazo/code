#!/usr/bin/env python

import os,glob


count = 0
cwd=os.getcwd()
for item in glob.glob(os.path.join(".", "*")) :
    if os.path.isfile(item) :
        print item + " is a file"
    elif os.path.isdir(item) :
        print item + " is a dir"  
        print item   
        os.chdir(item)
        if os.path.isfile(item) :
            print item + " is a file"
        elif os.path.isdir(item) :
            print item + " is a dir"
            os.chdir(cwd)
            print os.getcws() + " este el el dir"
    else :
        print "unknown"

