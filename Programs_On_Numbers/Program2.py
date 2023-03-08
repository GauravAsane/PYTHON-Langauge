# Accept one number from user and check whether is divisible by 5 or not


class Numbers:

	def __init__(self):
		self.Value = 0
		self.Flag = False

	def Accept(self):
		print("Enter the Number :")
		self.Value = int(input())

	def Check(self):

		if(self.Value % 5 == 0):

			self.Flag = True;

		else:

			self.Flag = False;


	def Display(self):

		if(self.Flag == True):

			print(str(self.Value)+" is divisible by 5");

		else:

			print(str(self.Value)+" is Not divisible by 5");




def main():
    obj = Numbers()
    obj.Accept()
    obj.Check()
    obj.Display()

if __name__ == "__main__":
    main()


