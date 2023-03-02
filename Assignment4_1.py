# using lambda function perform power of two
Power = lambda A: A**2

def main():
    print("Enter the element")
    No = int(input())
    
    Ans = Power(No)
    print("Power is :",Ans)


if __name__ == "__main__":
    main()