
# Accept two numbers from user and Divide that two numbers.
import sys

class Numbers:

    def __init__(self):
        self.iNo1 = 0
        self.iNo2 = 0
        self.iAns = 0

    def Accept(self):

        print("Enter the First Number :")
        self.iNo1 = int(input())

        print("Enter the Second Number :");
        self.iNo2 = int(input())


    def Division(self):

        self.iAns = self.iNo1 / self.iNo2

    def Display(self):

        if(self.iNo2 == 0.0):
            print("Error : Denominator number should not be 0.")
            sys.exit()

        else:
            print("Division is : "+str(self.iAns)+"\n")


def main():
    obj = Numbers()
    obj.Accept()
    obj.Division()
    obj.Display()

if __name__ == "__main__":
    main()
