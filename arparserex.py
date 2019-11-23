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

    args = parser.parse_args()  #Variable that contains all arguments
    #print vars(args)  ##Prints all arguments passed
    #print (args.string)

    with args.filepath as fp :  #From the variable args, use filepath as file input for search
            lines = args.filepath.readlines()
            for l in lines:
                if args.string in l:    #Variable string from args will be the string to search
                    print(l)

if __name__ == '__main__':  #Define main function
    filesearch()



