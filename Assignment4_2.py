# using lambda function perform multiplication

Mult = lambda Value1,Value2: Value1*Value2
   
def main():
    print("Enter first element")
    No1 = int(input())
    print("Enter second element")
    No2 = int(input())
    
    Ans = Mult(No1,No2)
    print("Multiplication is :",Ans)


if __name__ == "__main__":
    main()