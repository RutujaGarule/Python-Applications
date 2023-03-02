# recurssive program to return summation of its digits
# 879
# 24

def Summation(No):
    Sum = 0
    if(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10
        Summation(No)
    return Sum
    
  

def main():
    print("Enter number")
    Value = int(input())
    
    Ret = Summation(Value)
    print("Summation is : ",Ret)

if __name__ == "__main__":
    main()