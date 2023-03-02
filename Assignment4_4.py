# accept list from user and filter even numbers map function will calculate its square
# reduce will return addition of that numbers

def CheckEven(No):
    return (No%2 == 0)
    
def Square(No):
        return No*No
    
def Add(A,B):
    return A+B
    
    
def FilterX(Hepler_Function,Data):
    Result = []
    for No in Data:
        if(Hepler_Function(No)== True):
            Result.append(No)
    return Result       

def MapX(Hepler_Function,Data):
    Result = []
    for No in Data:
        Value = Hepler_Function(No)
        Result.append(Value)
    return Result

def ReduceX(Hepler_Function,Data):
    Ans = 0
    for No in Data:
        Ans = Hepler_Function(Ans,No)
    return Ans    

def main():
    print("Enter howmany elements you want")
    iSize = int(input())
    
    Input = []
    print("Enter the elements ")
    for i in range(0,iSize,1):
        Value = int(input())
        Input.append(Value)
        
    print("Elements from list are :",Input)
    
    Filter_Data = FilterX(CheckEven,Input)
    print("Data after filter is :",Filter_Data)
    
    MapX_Data = MapX(Square,Filter_Data)
    print("Data after map is :",MapX_Data)
    
    ReduceX_Data = ReduceX(Add,MapX_Data)
    print("Data after reduce is :",ReduceX_Data)


if __name__ == "__main__":
    main()