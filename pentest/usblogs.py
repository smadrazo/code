#!/usr/bin/env python

fdesc = open("/var/log/messages","r")
with fdesc as fp :
    lines = fdesc.readlines()
    c=0
    for l in lines:
        if 'USB' in l:
            print(l)
