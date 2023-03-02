def Frequency(Arr,No):
    Freq = 0
    for i in range(0,len(Arr),1):
        if(Arr[i] == No):
            Freq = Freq + 1
        
    return  Freq       

def main():
    print("Enter howmany elements you wnat to store")
    iSize = int(input())
    
    Input = []
    
    print("Enter the elements")
    for i in range(0,iSize,1):
        Value = int(input())
        Input.append(Value)
        
    print("Elements in list are :",Input)
    
    print("Enter number to find frequency")
    Value = int(input())
    
    Ans = Frequency(Input,Value)
    print("frequency of number is :",Ans)
        

if __name__ == "__main__":
    main()