
def Maximum(Arr):
    Max = 0
    Max = Arr[0]
    for i in range(0,len(Arr),1):
        if(Arr[i] > Max):
            Max = Arr[i]
            
    return Max        

def main():
    print("Enter the elements you want")
    iSize = int(input())
    
    Input = []
    
    print("Enter the elements of list")
    for iCnt in range(0,iSize,1):
        No = int(input())
        Input.append(No)
    
    print("Elements from list are :",Input)
    
    Ans = Maximum(Input)
    print("Maximum number is :",Ans)

if __name__ == "__main__":
    main()