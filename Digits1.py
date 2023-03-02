# count number of digits in number

def CountDigits(iNo):

    iDigit = 0
    
    print("inside CountDigits")
    if(iNo == 0):
        return 1
        
    if(iNo < 0):
        iNo = -iNo
        
    iCnt = 0    
    while(iNo != 0):
        iNo = iNo // 10
        iCnt = iCnt + 1
       
    return iCnt
    

def main():
    print("Enter number")
    iValue = int(input())

    iRet = CountDigits(iValue)
    print("number of digits are : ",iRet)



if __name__ == "__main__":
    main()
    
    
    
  