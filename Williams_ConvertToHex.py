import sys
import math
from decimal import *

strInput = 'exit'
strBinary = ''

def ReturnHexVal(intNum):
	#returns string with Hex value
	dictHexVals = { '10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F' }
	
	if intNum >= 0 and intNum <= 15:
		if intNum < 10:
			return str(intNum)
		else:
			return dictHexVals.get(str(intNum))
	else:
		return "error"
	
#END ReturnHexVal

def ConvertToHex(strNum):
	#Returns binary string of strNum
	strReturn = ''
	
	#integer conversion
	intNum = int(strNum)
	while intNum > 0:
		strReturn = ReturnHexVal(intNum % 16) + strReturn	#remainder value
		intNum = intNum // 16	#integer value
	
	return strReturn
#END ConvertToHex(strNum, bolDec)	
	
def main():
	while True:
		strInput = raw_input("Value to convert to binary: ")
		
		if strInput.lower() == 'exit':
			#Exit condition
			sys.exit()
		elif strInput == '':
			#error on no entry
			print "Must enter a value to convert."
			print "'exit' to quit program"
			print
		else:
			#not testing for correct alpha values
			if len(strInput) == strInput.count('0'):
				#nothing but 0's
				strHex = "0"
			else:
				strHex = ConvertToHex(strInput)
			print strHex
			print
#END main()
			
main()