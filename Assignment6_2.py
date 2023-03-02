
class BankAccount:
    
    ROI = 10.5
    
    def __init__(self):
        self.Name = ""
        self.Amount = 0
     
    def Display(self):
        print("Name of account holder is : ",self.Name)
        print("Amount in account of {} is : ".format(self.Name),self.Amount)

    def Deposit(self):
        print("Enter your name")
        self.Name = input()
        print("Enter the amount you want to deposite : ")
        Value = int(input())
        self.Amount = self.Amount + Value
        
    def Withdraw(self):
        print("Enter the amount you want to withdraw : ")
        Value = int(input())
        self.Amount = self.Amount - Value
        
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI * 1)/100
        print("Rate of interest is : ",Interest)
        
    

def main():

    obj1 = BankAccount()
    obj2 = BankAccount()
    
 
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()
    obj1.Display()
    
    obj2.Deposit()
    obj2.Withdraw()
    obj2.CalculateInterest()
    obj2.Display()
  


if __name__ == "__main__":
    main()