
class Bank_Account:
    
    Bank_Name = "HDFC bank pvt Ltd"
    ROI_On_FD = 6.7
    
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
        
    @classmethod
    def DisplayBankInformation(cls):
        print("welcomre to banking consloe")
        print("name of our bank is :",cls.Bank_Name)
        print("ROI on fixed deposit is :",cls.ROI_On_FD)
        
    
    @staticmethod
    def DisplayKYCInfo():
        print("please conside below KYC information")
        print("you have to submit below documents")
        print("1 : clear and recent passport size photo")
        print("2 : photo of adhar card")
        print("3 : photo of pan card")
        
    def Deposite(self,value):
        self.Amount = self.Amount + value
        
    def Withdraw(self,value):
        self.Amount = self.Amount - value


def main():

    Bank_Account.DisplayKYCInfo()
    
    print("name of bank is :",Bank_Account.Bank_Name)
    print("rate of interest on fixed deposit is :",Bank_Account.ROI_On_FD)
    
    Bank_Account.DisplayBankInformation()
    
    User1 = Bank_Account()
    User2 = Bank_Account()
    
    print("Creating first account")
    User1.CreateAccount()
    
    print("Creating second account")
    User2.CreateAccount()
    
    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()
    
    User1.Deposite(500)
    User2.Deposite(1200)
    
    print("amount of {} after deposite is {}".format(User1.Name,User1.Amount))
    print("amount of {} after deposite is {}".format(User2.Name,User2.Amount))
    
    User1.Withdraw(200)
    User2.Withdraw(3000)
    
    print("amount of {} after withdraw is {}".format(User1.Name,User1.Amount))
    print("amount of {} after withdraw is {}".format(User1.Name,User2.Amount))


if __name__ == "__main__":
    main()