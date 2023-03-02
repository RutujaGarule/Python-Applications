# accept number fron user,filter number which is greater tha equal to 70 and less than equal to 90
# map function increase eacg number by 10 and reduce will perform product of that
def CheckNum(No):
    if((No >= 70) and (No <= 90)):
        return True
def Add(No):
    return No +10        

def Mult(Ans,No):
    return Ans*No

   
def FilterX(Helper_Function,Data):
    Result = []
    for No in Data:
        if(Helper_Function(No) == True):
            Result.append(No)
    
    return Result

def MapX(Helper_Function,Data):
    Result = []
    for No in Data:
        Value = Helper_Function(No)
        Result.append(Value)
    return Result    

def ReduceX(Helper_Function,Data):
    Ans = 1
    for No in Data:
        Ans = Helper_Function(Ans,No)
    return Ans  

def main():
    print("Enter howmany elements you want")
    iSize = int(input())
    
    Input = []
    print("Enter the elements")
    for i in range(0,iSize,1):
        Value = int(input())
        Input.append(Value)
    print("Elements from the lis are :",Input) 

    FilterX_Data = FilterX(CheckNum,Input)
    print("Data after filter is :",FilterX_Data)
    
    MapX_Data = MapX(Add,FilterX_Data)
    print("Data after map is :",MapX_Data)
    
    ReduceX_Data = ReduceX(Mult,MapX_Data)
    print("Data after reduce is :",ReduceX_Data)
    



if __name__ == "__main__":
    main()