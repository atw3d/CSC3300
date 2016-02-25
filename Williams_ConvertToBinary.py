import sys
import math
from decimal import *

strInput = 'exit'
strBinary = ''

def ConvertToBinary(strNum, bolDec=False):
	#Returns binary string of strNum
	strReturn = ''
	
	if bolDec:
		#decimal conversion as well as integer
		strInt = strNum.split('.')[0]
		strDec = strNum.split('.')[1]
		
		intNum = int(strInt)
		while intNum > 0:
			strReturn = str(intNum % 2) + strReturn	#remainder value
			intNum = intNum // 2	#integer value
		strReturn = strReturn + '.'
		
		intDec = Decimal('0.'+strDec)	
		while intDec != 0:
			strReturn = strReturn + str((intDec * 2) // 1)	# decimal value
			intDec = (intDec * 2) % 1						# remainder value
						
			if len(strReturn) > 10:
				#max 10 characters
				if intDec != 0:
					strReturn = strReturn + " (rounded)"
				break
						
	else:
		#integer conversion
		intNum = int(strNum)
		while intNum > 0:
			strReturn = str(intNum % 2) + strReturn	#remainder value
			intNum = intNum // 2	#integer value

	
	return strReturn
#END ConvertToBinary(strNum, bolDec)	
	
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
		elif not strInput.isdigit():
			#test for decimal point
			strInputReplaceDecimal = strInput.replace('.','')
			if strInputReplaceDecimal.isdigit() and strInput.count('.') <= 1:
				#decimal
				if len(strInput) - 1 == strInput.count('0'):
					#nothing but 0's
					strBinary = "0.0"
				else:				
					strBinary = ConvertToBinary(strInput, True)
				print strBinary
				print
			else:
				#error on alpha entry
				print "Only numbers are accepted."
				print
		else:
			#integer
			if len(strInput) == strInput.count('0'):
				#nothing but 0's
				strBinary = "0"
			else:
				strBinary = ConvertToBinary(strInput)
			print strBinary
			print
#END main()
			
main()