
class Arithmatic:
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
        
        
    def Accept(self):
        print("Enter first number")
        self.Value1 = int(input())
        print("Enter second number")
        self.Value2 = int(input())
        
    def Addition(self):
        Result = self.Value1 + self.Value2
        return Result
        
    def Substraction(self):
        Result = self.Value1 - self.Value2
        return Result
        
    def Multiplication(self):
        Result = self.Value1 * self.Value2
        return Result
        
    def Division(self):
        Result = self.Value1 / self.Value2
        return Result
 

def main():

    obj1 = Arithmatic()
    obj2 = Arithmatic()
    
    obj1.Accept()
    Ans = obj1.Addition()
    print("Addition is : ",Ans)
    Ans = obj1.Substraction()
    print("Substraction is : ",Ans)
    Ans = obj1.Multiplication()
    print("Multiplication is : ",Ans)
    Ans = obj1.Division()
    print("Divisionis : ",Ans)
    
    obj2.Accept()
    Ans = obj2.Addition()
    print("Addition is : ",Ans)
    Ans = obj2.Substraction()
    print("Substraction is : ",Ans)
    Ans = obj2.Multiplication()
    print("Multiplication is : ",Ans)
    Ans = obj2.Division()
    print("Divisionis : ",Ans)


if __name__ == "__main__":
    main()