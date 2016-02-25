#!/usr/bin/python

import sys

def main():
    flNames = open("name.txt", "r")
    lstMasterNames = []
    
    for strLine in flNames:
		strLine = strLine.rstrip()
		strLastFirst = strLine.split(' ')[1] + ',' + strLine.split(' ')[0]
		lstMasterNames.append(strLastFirst)
		
    lstMasterNames.sort()
    
    for strName in lstMasterNames:
        print strName
        
#end Main()

main()

print
while True:
	if raw_input("exit: "):
		sys.exit()
