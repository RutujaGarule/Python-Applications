print("application to demonstrate industrial programming")

def Addition(value1, value2):
    Ans = value1 + value2
    return Ans
    
def main():
    print("enter first number : ")
    no1 = int(input())
    print("enter second number : ")
    no2 = int(input())
    
    Ret = Addition(no1 ,no2)
    
    
    print("addition is : ",Ret)
    
if __name__ == "__main__":   
    main()