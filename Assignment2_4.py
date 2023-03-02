# accept number and disply addition of its factors
def Factors(No):
    Result = []
    for i in range(1,int(No/2)+1,1):
        if(No%i == 0):
            Result.append(i)
    return Result

def Add(Arr):
    Sum = 0
    for No in Arr:
        Sum = Sum + No
    return Sum

def main():
    print("Enter Number")
    Value = int(input())
    
    Ans = Factors(Value)
    print("Factors are :",Ans)
    
    Ret = Add(Ans)
    print("Addition is :",Ret)

if __name__ == "__main__":
    main()