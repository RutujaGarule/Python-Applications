print("Check number is divisible by 5")

def Divisible(Value):
    if((Value%5)== 0):
        return True
    else:
        return False
    

def main():
    print("enter the number")
    No = int(input())
    Ret = Divisible(No)
    print(Ret)
    
    
if __name__ == "__main__":
    main()