# python application contains two threads as even and odd .even thread will display first 10 even number
#odd thread will display first 10 odd numbers

import os
import threading
import time

def Even(No):
    for i in range(0,No,1):
        if(i % 2 == 0):
            print("Even number is : ",i)
 
def Odd(No):
    for i in range(0,No,1):
        if(i % 2 != 0):
            print("Odd number is : ",i)

def main():
    Value = 20
    
    T1 = threading.Thread(target = Even,args = (Value,))
    T2 = threading.Thread(target = Odd,args = (Value,))
        
    T1.start()
    T2.start()
    
    T1.join()
    T2.join()


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",(end_time - start_time))