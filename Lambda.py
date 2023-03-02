
def Add(No1,No2):
    return No1+No2

addFunction = lambda A,B : A+B

Ans1 = Add(10,11)
Ans2 = addFunction(10,11)

print("Addition using normal function :",Ans1)
print("Addition using lambda function :",Ans2)

print("tyoe of lambda function is :",type(addFunction))




