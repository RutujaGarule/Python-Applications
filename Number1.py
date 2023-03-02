
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

def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()
    

if __name__ == "__main__":
    main()