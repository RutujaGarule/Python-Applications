
class Arithmatic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Add(self):
        return self.No1+self.No2

    def Sub(self):
        return self.No1-self.No2

 
def main():
    print("enter first number")
    No1 = int(input())
    
    print("enter second number")
    No2 = int(input())

    obj = Arithmatic(No1,No2)
    
    Ans = obj.Add()
    print("addition is :",Ans)
    
    
    Ans = obj.Sub()
    print("substractions is :",Ans)

if __name__ == "__main__":
    main()