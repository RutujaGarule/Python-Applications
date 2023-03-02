#  Thread1 display 1 to 50 on screen and Thread2 dispaly 50 to 1 in reverse order
# after execution of thread1 gets completed the schedule thread2


import os
import time
import threading

def Display(No):
    for i in range(1,No+1,1):
        print(i)

def Reverse(No):
    for i in range(No,0,-1):
        print(i)

def main():

    Value = 50

    T1 = threading.Thread(target = Display,args = (Value,))
    T2 = threading.Thread(target = Reverse,args = (Value,))
    
    T1.start()
    T1.join()
    
    T2.start()
    T2.join()
    
    print("Exit from main")
    


if __name__ == "__main__":
    main()