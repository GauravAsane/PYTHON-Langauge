# Accept one number from user and display its summation of all non factors on screen.

import sys

class Numbers:

	def __init__(self):
		self.iValue = 0


	def Accept(self):
		print("Enter the Number :")
		self.iValue = int(input())



	def NonFactSum(self):

		iCnt = 0
		iMult = 1
		iSum = 0

		if(self.iValue <= 0):

			print("Enter valid number")
			Sys.exit()


		for iCnt in range(1 , self.iValue ,1):

			if( self.iValue % iCnt != 0):

				iSum = iSum + iCnt;		


		return iSum
			


	def Display(self):

		iRet = self.NonFactSum()
		print("Addition of non factors of "+str(self.iValue)+" is : "+str(iRet))
			

def main():
	obj = Numbers()
	obj.Accept()
	obj.Display()

if __name__ == "__main__":
    main()

