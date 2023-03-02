print("Check number is positive or negative")

def Check(Value):
    if(Value > 0):
        print("Number is positive")
    elif(Value == 0):
        print("number is zero")
    else:
        print("number is negative")
    

def main():
    print("enter the number")
    No = int(input())
    Check(No)
    
if __name__ == "__main__":
    main()