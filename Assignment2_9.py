print("number of digits in number")

def Digits(Value):
    return len(Value)
    
    
    
def main():
    print("Enter the number")
    No = input()
    
    Ans = Digits(No)
    print("number of digits are :",Ans)
    
if __name__ == "__main__":
    main()