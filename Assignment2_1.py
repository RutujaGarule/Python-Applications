print("Arithmatic Operations")

import Arithmatic 

def main():
    print("Enter first number")
    No1 = int(input())
    print("Enter second number")
    No2 = int(input())
    
    Ans = Arithmatic.Add(No1,No2)
    print("Addition is ",Ans)
    
    Ans = Arithmatic.Sub(No1,No2)
    print("Substraction is ",Ans)
    
    Ans = Arithmatic.Mult(No1,No2)
    print("Multiplication is ",Ans)
    
    Ans = Arithmatic.Div(No1,No2)
    print("Division is ",Ans)

if __name__ == "__main__":
    main()