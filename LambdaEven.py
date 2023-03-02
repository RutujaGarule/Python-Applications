
def CheckEven(No):
    if(No%2 == 0):
        return True
    else:
        return False     
 
def CheckEvenX(No):
    return (No % 2 == 0)

CheckEvenXX = lambda No : No %2 == 0
 
Ret = CheckEvenXX(12) 

if(Ret == True):
    print("its even")
else:
    print("its odd")    