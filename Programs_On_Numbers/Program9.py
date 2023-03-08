# Accept one number from user and display its multiplication of factors on screen.

import sys

class Numbers:

	def __init__(self):
		self.iValue = 0


	def Accept(self):
		print("Enter the Number :")
		self.iValue = int(input())

	def MultFact(self):

		iCnt = 0
		iMult = 1

		if(self.iValue <= 0):

			print("Enter valid Number");
			Sys.exit()


		for iCnt in range (1 ,int(self.iValue/2)+1 , 1):

			if( self.iValue % iCnt == 0):

				iMult = iMult * iCnt

		return iMult


	def Display(self):

		iRet = self.MultFact()

		print("Multiplication of factors of "+str(self.iValue)+" is : "+str(iRet))


def main():
	obj = Numbers()
	obj.Accept()
	obj.Display()

if __name__ == "__main__":
    main()
