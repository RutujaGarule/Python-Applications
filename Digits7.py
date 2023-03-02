# chk palindrome using two functions

def Reverse(iNo):
 
    iDigit = 0
    iRev = 0
   
    while(iNo != 0):
        iDigit = iNo % 10
        iRev = (iRev * 10)+ iDigit
        iNo = iNo // 10
    return iRev
    
def ChkPalindrome(iNo):
    if(iNo < 0):
        iNo = -iNo
        
    iReverse = Reverse(iNo)
    if(iReverse == iNo):
        return True
    else:
        return False
    

def main():
    print("Enter number :")
    iValue = int(input())

    iRet = ChkPalindrome(iValue)
    if(iRet == True):
        print("{} is palindrome number".format(iValue))
    else:
        print("{} is not palindrome number".format(iValue))
    


if __name__ == "__main__":
    main()