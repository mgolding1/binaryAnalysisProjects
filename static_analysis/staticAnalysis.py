#!/usr/local/bin/python3.8

import pefile
import sys

print("Begining...")

#TODO validate the args
if ((len(sys.argv) > 1) and (len(sys.argv) < 3)) :
    pe =  pefile.PE(sys.argv[1])
else:
    print("Please specify a PE file")
    print("Usage: ./static_analysis /path/to/pe_file")

#If the file is too big use the line bellow. 
#This will prevent parsing the directories
#pe =  pefile.PE(‘/path/to/pefile.exe’, fast_load=True)

#TODO Answer Lab 1 questions
#   Does the file match any known signatures
#   When were the files compiled
#   Is this file packed or obfuscated
#   What are the notable imports and what could they do
#   What are the host and network based indicators
#   What could this file do?



