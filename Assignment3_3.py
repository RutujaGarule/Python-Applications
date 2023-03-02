
def Minimum(Arr):
    Min = 0
    Min = Arr[0]
    for i in range(0,len(Arr),1):
        if(Arr[i] < Min):
            Min = Arr[i]
    return Min    


def main():
    print("Enter howmany elements you want")
    iSize = int(input())
    
    Input = []
    print("Enter the elements")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Input.append(Value)
        
    print("Elements of list are :",Input)

    Ans = Minimum(Input)
    print("Minimum number is :",Ans)


if __name__ == "__main__":
    main()