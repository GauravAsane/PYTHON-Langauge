# Accept one number from user if number is less than 10 then print "Hello" otherwise print "Demo".



class Numbers:

	def __init__(self):
		self.Value = 0
		self.Flag = False

	def Accept(self):
		print("Enter the Number :")
		self.Value = int(input())

	def Display(self):

		if(self.Value < 10):

			print("Hello");

		else:

			print("Demo");


def main():
	obj = Numbers()
	obj.Accept()
	obj.Display()

if __name__ == "__main__":
    main()


