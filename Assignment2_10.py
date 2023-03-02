#addition of digits

def AddDigits(iNo):
    iDigits = 0
    iSum = 0
    
    if(iNo < 0):
        iNo = -iNo
        
    while(iNo != 0):
        iDigits = iNo % 10
        iSum = iSum + iDigits
        iNo = iNo // 10
        
    return iSum


def main():
    print("Enter the number")
    iValue = int(input())

    iRet = AddDigits(iValue)
    print("Addition of digits are : ",iRet)


if __name__ == "__main__":
    main()