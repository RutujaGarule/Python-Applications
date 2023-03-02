
class Bank_Account:
    
    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0
        
    def CreateAccount(self):
        print("enter your name :")
        self.Name = input()
        
        print("enter your initial amount :")
        self.Amount = int(input())
        
        print("enter your Address :")
        self.Address = input()
        
        print("enter your account number :")
        self.AccountNo = int(input())
        
        
    def DisplayAccountInfo(self):
        print("-----your account information is as below :------")
        print("name of account holder :",self.Name)
        print("address of account holder :",self.Address)
        print("current amount in account  :",self.Amount)
        print("account number is :",self.AccountNo)
        
    
    



def main():
    User1 = Bank_Account()
    User2 = Bank_Account()
    
    print("Creating first account")
    User1.CreateAccount()
    
    print("Creating second account")
    User2.CreateAccount()
    
    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()



if __name__ == "__main__":
    main()