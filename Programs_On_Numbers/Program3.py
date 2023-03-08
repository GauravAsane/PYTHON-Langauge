# Accept number from user and check whether is Even or odd


class Numbers:

	def __init__(self):
		self.Value = 0
		self.Flag = False

	def Accept(self):
		print("Enter the Number :")
		self.Value = int(input())


	def CheckEven(self):

		if(self.Value % 2 == 0):

			self.Flag = True

		else:

			self.Flag = False


	def Display(self):

		if(self.Flag == True):

			print(str(self.Value)+" is Even Number.")

		else:
			print(str(self.Value) + " is Odd Number.")



def main():
	obj = Numbers()
	obj.Accept()
	obj.CheckEven()
	obj.Display()

if __name__ == "__main__":
    main()


