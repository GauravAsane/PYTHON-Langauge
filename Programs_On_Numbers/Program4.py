# Accept number from user and print that number of * on screen

import sys

class Numbers:

	def __init__(self):
		self.Value = 0
		self.Flag = False

	def Accept(self):
		print("Enter the Number :")
		self.Value = int(input())


	def Display(self):
		iCnt = 0
		if(self.Value < 0):

			print("Enter Valid Number");
			sys.exit()

		for iCnt in range(0,self.Value,1):
			print("*\t",end = ' ')


def main():
	obj = Numbers()
	obj.Accept()
	obj.Display()

if __name__ == "__main__":
    main()


