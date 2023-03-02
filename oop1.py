
class Arithmatic:
    
    def __init__(self,A,B):
        print("inside init method")
        self.No1 = A
        self.No2 = B
        
    def Add(self):
        Ans = self.No1 + self.No2
        return Ans
        
    def Sub(self):
        Ans = self.No1 - self.No2
        return Ans    

def main():
    print("inside main method")
    
    obj = Arithmatic(11,10)
    Output = obj.Add()
    print("Addition is : ",Output)
    
    Output = obj.Sub()
    print("Substraction is : ",Output)
    
    objX = Arithmatic(21,20)
    



if __name__ == "__main__":
    print("inside starter")
    main()