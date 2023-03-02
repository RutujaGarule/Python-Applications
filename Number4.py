
class Numbers:
    def __init__(self):
        self.Size = 0
        self.Arr = list()
        
    def Accept(self):
        print("enter howmany elements you want")
        self.Size = int(input())
        
        print("enter the elements")
        Value = 0
        for i in range(0,self.Size):
            Value = int(input())
            self.Arr.append(Value)
    
    def Display(self):
        print("elements in list are :")
        for i in range(0,self.Size):
            print(self.Arr[i])
            
    def Summation(self):
        Sum = 0
        for i in range(0,self.Size):
            Sum = Sum + self.Arr[i]
        
        return Sum
        
             
    def Average(self):
        Sum = 0
        for i in range(0,self.Size):
            Sum = Sum + self.Arr[i]
        
        return (Sum/self.Size)   
        
             
    def Maximum(self):
        Max = self.Arr[0]
        for i in range(0,self.Size):
            if(self.Arr[i] > Max):
                Max = self.Arr[i]
            
        return Max


def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()
    
    Output = obj.Summation()
    print("Summation of all elements is : ",Output)
    
    Output = obj.Average()
    print("Average of all elements is : ",Output)
    
    Output = obj.Maximum()
    print("Maximum number is : ",Output)
    

if __name__ == "__main__":
    main()