# check number is divisible by 3 and 5

def CheckDivisible(No):
    if(No%3 == 0):
        if(No%5 == 0):
            return True
        else:
            return False    

def main():
    print("Enter number")
    Value = int(input())
    
    Ret = CheckDivisible(Value)
    if(Ret == True):
        print(Value,"Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")
            
if __name__ == "__main__" :
    main()