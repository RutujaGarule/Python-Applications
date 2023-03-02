
class Demo:
    
    Value = 0
    
    def __init__(self,value1,value2):
        self.No1 = value1
        self.No2 = value2

    def Fun(self):
        print("Values of instance variables are : ",self.No1,self.No2)
        
    def Gun(self):
        print("Values of instance variables are : ",self.No1,self.No2)
        

def main():

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)
    
    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()


if __name__ == "__main__":
    main()