def ChkNum(No):
    if((No%2)==0):
        print("Number is Even")
    else:
        print("Number is Odd")
    
def main():
    print("Enter Number")
    Value = int(input())
    ChkNum(Value)
    
if __name__ == "__main__":
    main()