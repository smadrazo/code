#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :filesearch.py
#description     :This program search a string on a file, providing both values on the arguments
#author          :
#date            :
#version         :1.0
#usage           : filesearch.py 
#notes           :
#python_version  :2.7.6  
#=======================================================================

import argparse,sys,os

def filesearch():    ##Defines module filesearch()
    os.system('clear')
    parser = argparse.ArgumentParser(description='Search within a File')
    group = parser.add_argument_group('Required variables')
    group2 = parser.add_argument_group('Required variables')
    group.add_argument('--string', help='String to search', required=True)    #Default type=str
    group.add_argument('--filepath', help='Filename',nargs='?',type=argparse.FileType('r'), required=True)
    group2.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()
    #print vars(args)  ##Prints all arguments passed
    #print (args.string)

    with args.filepath as fp :
            lines = args.filepath.readlines()
            for l in lines:
                if args.string in l:
                    print(l)

if __name__ == '__main__':  #Define main function
    filesearch()


#>>> import argparse
#>>> 
#>>> parser = argparse.ArgumentParser(description='Search within a File')
#>>> parser.add_argument('--string', help='String to search', required=True)    #Default type=str
#_StoreAction(option_strings=['--string'], dest='string', nargs=None, const=None, default=None, type=None, choices=None, help='String to search', metavar=None)
#>>> parser.add_argument('--filepath', help='Filename',nargs='?',type=argparse.FileType('r'), required=True) 
#_StoreAction(option_strings=['--filepath'], dest='filepath', nargs='?', const=None, default=None, type=FileType('r'), choices=None, help='Filename', metavar=None)
#>>> parser.add_argument('--version', action='version', version='%(prog)s 1.0')
#_VersionAction(option_strings=['--version'], dest='version', nargs=0, const=None, default='==SUPPRESS==', type=None, choices=None, help="show program's version number and exit", metavar=None)
#>>> 
#>>> 
#>>> 
#>>> parser.parse_args(['--string','hola','--filepath','/var/log/system.log'])
#Namespace(filepath=<open file '/var/log/system.log', mode 'r' at 0x10e27f660>, string='hola')