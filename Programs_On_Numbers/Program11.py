# Accept one number from user and display its all non factors on screen.

import sys

class Numbers:

	def __init__(self):
		self.iValue = 0


	def Accept(self):
		print("Enter the Number :")
		self.iValue = int(input())


	def DisplayNonFact(self):

		iCnt = 0
		iMult = 1

		if(self.iValue <= 0):

			print("Enter valid number")
			Sys.exit()


		print("Non Factors of "+str(self.iValue))

		for iCnt in range( 1 ,self.iValue ,1):

			if( self.iValue % iCnt != 0):

				print(str(iCnt)+"\t",end = ' ')


def main():
	obj = Numbers()
	obj.Accept()
	obj.DisplayNonFact()


if __name__ == "__main__":
    main()
