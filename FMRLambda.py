
CheckEven = lambda No:(No%2 == 0)
    

Doubles = lambda No: No*2
    

Sum = lambda A,B: A+B
    
    

def filterX(Helper_Function,Data):
    Result = []
    for No in Data:
        if(Helper_Function(No)==True):
            Result.append(No)
        
    return Result

def mapX(Helper_Function,Data):
    Result = []
    for No in Data:
        Value = Helper_Function(No)
        Result.append(Value)
    return Result    

def reduceX(Helper_Function,Data):
    Ans = 0
    for No in Data:
        Ans = Helper_Function(Ans,No)
    return Ans    

def main():
   print("enter the elements you want :")
   iSize = int(input())
   
   Data_Input = []
   print("enter the data :")
   for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
        
   print("data is :",Data_Input)

   Data_Filter = filterX(CheckEven,Data_Input)
   
   print("data after filter is :",Data_Filter)
    
   Data_map = mapX(Doubles,Data_Filter)
   print("data after map is :",Data_map)
   
   Output = reduceX(Sum,Data_map)
   print("result after reduce is :",Output)
    
    

if __name__ == "__main__":
    main()