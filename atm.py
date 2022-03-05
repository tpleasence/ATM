class atm:
    def __init__(self, cardNumber, pinNumber):
     self.cardNumber = cardNumber

     self.pinNumber = pinNumber

    def checkbalance(self):
        print ("balanceprinted")
    
    def withdraw(self):
        print ("withdrawprinted")

def main():
    cardNumber = input("typecardnumber = ")
   

if __name__ == "__main__":
    main()