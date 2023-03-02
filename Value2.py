
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



def main():
    print("enter number")
    A = int(input())
    
    obj = Value(A)
    
    Ret = obj.ChkPerfect()
    if(Ret == True):
        print("{} is perfect number".format(A))
    else:
        print("{} is not perfect number".format(A))


if __name__ == "__main__":
    main()