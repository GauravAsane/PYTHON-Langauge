# Accept two numbers from user and display first number in second number of times.



class Numbers:


	def __init__(self):
		self.iValue1 = 0
		self.iFreq = 0


	def Accept(self):
		print("Enter the Number :")
		self.Value = int(input())


	def Accept(self):

		print("Enter the First Number :")
		self.iValue1 = int(input())

		print("Enter the Second Number :")
		self.iFreq= int(input())


	def Display(self):

		iCnt = 0

		if(self.iFreq < 0):

			print("Enter Positive Frequency Number");
			sys.exit()


		for iCnt in range(0, self.iFreq ,1):

			print(self.iValue1,end = ' ')


def main():
	obj = Numbers()
	obj.Accept()
	obj.Display()

if __name__ == "__main__":
    main()


