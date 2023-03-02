# addition of digits

def SumDigits(iNo):

    iDigit = 0
    iSum = 0
    
    print("inside SumDigits")
    
    if(iNo < 0):
        iNo = - iNo
    
    while(iNo != 0):
        iDigit = iNo % 10
        iSum = iSum + iDigit
        iNo = iNo // 10
        
    return iSum

def main():
    print("Enter number")
    iValue = int(input())

    iRet = SumDigits(iValue)
    print("Summation of digits is : ",iRet)



if __name__ == "__main__":
    main()
    
    
    
  