# Maximum digit in number

def ChkMax(iNo):
    if(iNo < 0):
        iNo = -iNo
        
    iDigit = 0
    iMax = 0
    
    while(iNo != 0):
        iDigit = iNo % 10
        if(iDigit > iMax):
            iMax = iDigit
        iNo = iNo // 10
    
    return iMax
    


def main():
    print("Enter number :")
    iValue = int(input())

    iRet = ChkMax(iValue)
    print("{} is Maximum digit".format(iRet))


if __name__ == "__main__":
    main()