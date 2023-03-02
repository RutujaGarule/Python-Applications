# Accept number and return its factorial
def Factorial(No):
    Ans = 1
    for i in range(No,1,-1):
        Ans = Ans*i
    return Ans
    


def main():
    print("Enter number")
    Value = int(input())
    
    Ret = Factorial(Value)
    print("Factorial is :",Ret)


if __name__ == "__main__":
    main()