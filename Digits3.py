# count even digits in number

def CountEvenDigits(iNo):

    iDigit = 0
    iCnt = 0
    
    print("inside CountDigits")
    if(iNo == 0):
        return 1
        
    if(iNo < 0):
        iNo = -iNo
        
    while(iNo != 0):
        iDigit = iNo % 10
        if((iDigit % 2) == 0):
            iCnt = iCnt + 1
        iNo = iNo // 10
        
    return iCnt

def main():
    print("Enter number")
    iValue = int(input())

    iRet = CountEvenDigits(iValue)
    print("number of digits are : ",iRet)



if __name__ == "__main__":
    main()
    
    
    
  