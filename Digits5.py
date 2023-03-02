# check palindrome using for loop
# wrong output

def ChkPalindrome(iNo):
    if(iNo < 0):
       iNo = -iNo
        
    iTemp = iNo
    iDigit = 0
    iRev = 0

    for i in range(iNo,(iNo!=0),iNo//10):
        iDigit = iNo % 10
        iRev = (iRev * 10)+ iDigit
        #iNo = iNo // 10
       
    if(iRev == iTemp):
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