print("application to demonstrate industrial programming")

import module
    
def main():
    print("value of __name__ from main is :",__name__)
    
    print("enter first number : ")
    no1 = int(input())
    print("enter second number : ")
    no2 = int(input())
    
    Ret = module.Addition(no1 ,no2)
    
    
    print("addition is : ",Ret)
    
if __name__ == "__main__":   
    main()