 # Accept one number from user and display that number of even numbers on screen.

import sys

class Numbers:

	def __init__(self):
		self.Value = 0


	def Accept(self):
		print("Enter the Number :")
		self.Value = int(input())



	def DisplayEven(self):

		iCnt = 0

		if(self.Value < 0):

			print("Enter valid number")
			sys,exit()


		print("Even Numbers are : ")

		for iCnt in range(2 , self.Value*2+2 , 2):

			if(iCnt % 2 == 0):

				print(str(iCnt)+"\t",end = ' ')


def main():
	obj = Numbers()

	obj.Accept();
	obj.DisplayEven();

if __name__ == "__main__":
    main()

