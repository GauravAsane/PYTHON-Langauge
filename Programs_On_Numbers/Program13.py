# Accept one number from user and display difference between summation of all  its factors and non factors on screen.

import sys

class Numbers:

	def __init__(self):
		self.iValue = 0


	def Accept(self):
		print("Enter the Number :")
		self.iValue = int(input())



	def FactDiff(self):

		iCnt = 0
		iSum1 = 0
		iSum2 = 0
		diff = 0

		if(self.iValue <= 0):

			print("Enter valid number")
			Sys.exit()


		for iCnt in range(1 , self.iValue , 1):

			if( self.iValue % iCnt != 0):

				iSum1 = iSum1 + iCnt

			else:

				iSum2 = iSum2 + iCnt



		diff = iSum2 - iSum1
		return diff


	def Display(self):

		iRet = self.FactDiff()

		print("Difference of factors and non factors of "+str(self.iValue)+" is : "+str(iRet))
		


def main():
	obj = Numbers()
	obj.Accept()
	obj.Display()

if __name__ == "__main__":
    main()
