
def Demo1():
    print("Inside Demo1")

def Demo2(No):
    print("Inside Demo2 with parameter : ",No)

def Demo3(No):
    print("Inside demo3 with argument : ",No)
    return No+2

def Demo4(No1,No2):
    print("Inside Demo4")
    Add = No1 + No2
    return Add

def Demo5(No1,No2):
    print("inside Demo5")
    Add = No1 + No2
    Sub = No1 - No2
    return Add,Sub

def main():
    Demo1()
    Demo2("Hello")
    Ans = Demo3(10)
    print("return value of Demo3 is :",Ans)
    Ans = Demo4(10,11)
    print("return value of demo4 is :",Ans)
    Ans1,Ans2 = Demo5(11,10)
    print("First return value :",Ans1)
    print("second return value :",Ans2)
    

if __name__ == "__main__":
    main()