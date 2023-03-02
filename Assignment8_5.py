# recurssive program to calculate factorial
# 5
# 120

def Fact(No):
    if(No <= 0):
        return 1
    else:
        return(No * Fact(No -1))
    
def main():
    print("Enter number")
    Value = int(input())
    
    Ret = Fact(Value)
    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()