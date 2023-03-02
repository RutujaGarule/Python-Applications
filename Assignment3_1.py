
def Add(Arr):
    Sum = 0
    for No in Arr:
        Sum = Sum + No
    return Sum
    

def main():
    print("Enter the elements you want")
    iSize = int(input())
    
    Input = []
    
    print("Enter the elements of list")
    for iCnt in range(0,iSize,1):
        No = int(input())
        Input.append(No)
    
    print("Elements from list are :",Input)
    
    Ans = Add(Input)
    print("Addition is :",Ans)
    
        

if __name__ == "__main__":
    main()