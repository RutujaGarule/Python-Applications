
class Arithmatic:

    def __init__(self):
        self.Value = 0   
            
    
    def Factors(self):
        Fact = []
        for i in range(1,int(self.Value/2)+1,1):
            if((self.Value % i) == 0):
                Fact.append(i)
        return(Fact)
        
    def SumFactors(self):
        Sum = 0
        for i in range(1,int(self.Value/2)+1,1):
            if((self.Value % i) == 0):
                Sum = Sum + i
        return Sum
        
    def ChkPerfect(self,Helper_Function):
        Ans = Helper_Function()
        if(Ans == self.Value):
            return True
        else:
            return False
        
        
    def ChkPrime(self):
        i = 0
        Flag = True

        for i in range(2,int(self.Value / 2) + 1):
            if(self.Value % i == 0):
                Flag = False
                break
        
        return Flag
            
        
    def Accept(self):
        print("Enter the number")
        self.Value = int(input())
        

def main():

    obj1 = Arithmatic()
    obj1.Accept()
    
    Ret = []
    Ret = obj1.Factors()
    print("Factors are : ",Ret)
    
    Ret = obj1.SumFactors()
    print("Summation of factors is : ",Ret)
    
    Ret = obj1.ChkPerfect(obj1.SumFactors)
    if(Ret == True):
        print("Number is perfect number")
    else:
        print("Number is not perfect number")
    
    Ret = obj1.ChkPrime()
    if(Ret == True):
        print("Number is prime number")
    else:
        print("Number is not prime number")


if __name__ == "__main__":
    main()