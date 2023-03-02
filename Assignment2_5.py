# prime or not

def ChkPrime(iNo):
    Flag = True
    
    if((iNo % 2) == 0):
        Flag = False
        
    for iCnt in range(2,int(iNo/2)+1,1):
        if(iNo % iCnt == 0):
            Flag = False
            break
            
    return Flag
        


def main():
    print("Enter number you want")
    iValue = int(input())

    iRet = ChkPrime(iValue)
    if(iRet == False):
        print("{} is not prime number".format(iValue))
    else:
        print("{} is prime number".format(iValue))
    
if __name__ == "__main__":
    main()