# accept list from user and filter prime numbers and map will multiply each number by 2
#reduce will return maximum number 

def ChkPrime(No):
    Flag = True
    for i in range(2,int(No/2)+1,1):
        if((No % i) == 0):
            Flag = False
            break
    return Flag

def Multiply(No):
    return No *2
    
def Maximum(Data):
    for i in range(0,len(Data),1):
        Max = Data[0]
        if(Data[i] > Max):
            Max = Data[i]
    return Max   
            

def FilterX(HelperFunction,Data):
    Result = []
    for No in Data:
        if(HelperFunction(No)== True):
           Result.append(No)
    return Result        
            
def MapX(HelperFunction,Data):
    Result = []
    for No in Data:
        Value = HelperFunction(No)
        Result.append(Value)
    return Result

def ReduceX(HelperFunction,Data):
    
    Max = HelperFunction(Data)
    return Max
    

def main():
    print("Enter number you want to store")
    iSize = int(input())
    
    Input = []
    print("Enter numbers")
    for i in range(0,iSize,1):
        Value = int(input())
        Input.append(Value)
    print("Elements of list are : ",Input)
    
    FilterData = FilterX(ChkPrime,Input)
    print("data after filter is : ",FilterData)
    
    MapData = MapX(Multiply,FilterData)
    print("Data after map is : ",MapData)
    
    ReduceData = ReduceX(Maximum,MapData)
    print("Data after reduce is : ",ReduceData)




if __name__ == "__main__":
    main()