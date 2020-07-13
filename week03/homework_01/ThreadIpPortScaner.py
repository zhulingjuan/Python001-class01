# https://blog.csdn.net/IChocolateKapa/article/details/23941967
# https://stackoverflow.com/questions/2953462/pinging-servers-in-python

#coding:gbk


#!/usr/bin/env python3.5
import urllib.request
import getopt
import sys

opts,args = getopt.getopt(sys.argv[1:],'-h-f:-v',['help','filename=','version'])
for opt_name,opt_value in opts:
    if opt_name in ('-h','--help'):
        print("[*] Help info")
        exit()
    if opt_name in ('-v','--version'):
        print("[*] Version is 0.01 ")
        exit()
    if opt_name in ('-f','--filename'):
        fileName = opt_value
        print("[*] Filename is ",fileName)
        # do something
        exit()