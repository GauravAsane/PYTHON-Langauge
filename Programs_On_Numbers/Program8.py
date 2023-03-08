#  Accept one number from user and display even factors of that number on screen.


class Numbers :

	def __init__(self):
		self.iValue = 0


	def Accept(self):
		print("Enter the Number :")
		self.iValue = int(input())


	def DisplayEvenFact(self):

		iCnt = 0

		if(self.iValue <= 0):

			print("Enter valid number");
			sys.exit()

		print("Even Factors are : ")
		for iCnt in range(2 ,int(self.iValue/2)+1 ,2):
		
			if( self.iValue % iCnt == 0):

				if(iCnt % 2 == 0):

					print(str(iCnt)+"\t",end = ' ')



def main():
	obj = Numbers()

	obj.Accept();
	obj.DisplayEvenFact();

if __name__ == "__main__":
    main()



