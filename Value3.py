
class Value:

    def __init__(self,Data):
        self.No = Data
        
    def SumFactor(self):
        Sum = 0
        
        for i in range(1,int(self.No/2)+1):
            if(self.No % i == 0):
                Sum = Sum + i
        return Sum 

    def ChkPerfect(self):
        Ans = self.SumFactor()
        
        if(self.No == Ans):
            return True
        else:
            return False

    def ChkPrime(self):
        Ans = self.SumFactor()
        
        if(Ans == 1):
            return True
        else:
            return False

def main():
    print("enter number")
    A = int(input())
    
    obj = Value(A)
    
    Ret = obj.ChkPrime()
    if(Ret == True):
        print("{} is prime number".format(A))
    else:
        print("{} is not prime number".format(A))
        
    


if __name__ == "__main__":
    main()