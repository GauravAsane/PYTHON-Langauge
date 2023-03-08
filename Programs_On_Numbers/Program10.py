# Accept one number from user and display its factors in decreasing order on screen.

import sys

class Numbers:

	def __init__(self):
		self.iValue = 0


	def Accept(self):
		print("Enter the Number :")
		self.iValue = int(input())



	def DisplayFactRev(self):

		iCnt = 0
		iMult = 1

		if(self.iValue <= 0):

			print("Enter valid number")
			System.exit(0);


		print("Reverse Factors of "+str(self.iValue)+" is : ")

		for iCnt in range(self.iValue-1 ,0 ,-1):

			if( self.iValue % iCnt == 0):

				print(str(iCnt)+"\t",end = ' ')


def main():
	obj = Numbers()
	obj.Accept()
	obj.DisplayFactRev()


if __name__ == "__main__":
    main()

