# Application to find maximum number

def Maximum(No1,No2):
   if No1 > No2:
        return No1
   else:
        return No2
    
def main():
    print("enter first number")
    Value1 = input()
    print("enter second number")
    Value2 = input()
    
    Ans = Maximum(int(Value1),int(Value2))
    
    print("Largest number is :",Ans)

if __name__ == "__main__":
    main()
