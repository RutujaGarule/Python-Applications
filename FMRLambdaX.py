from functools import reduce

CheckEven = lambda No:(No%2 == 0)  

Doubles = lambda No: No*2    

Sum = lambda A,B: A+B
    

def main():
   print("enter the elements you want :")
   iSize = int(input())
   
   Data_Input = []
   print("enter the data :")
   for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
        
   print("data is :",Data_Input)

   Data_Filter = list(filter(CheckEven,Data_Input))
   
   print("data after filter is :",Data_Filter)
    
   Data_map = list(map(Doubles,Data_Filter))
   print("data after map is :",Data_map)
   
   Output = reduce(Sum,Data_map)
   print("result after reduce is :",Output)


if __name__ == "__main__":
    main()