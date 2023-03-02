# python application contains two threads as evenfactor and oddfactor .Both threads accept oane parameter as integer
# Evenfactor thread will display addtion of evenfactors and oddfactor will display addition of odd factors
# After execution of both thread gets completed main thread will display "exit from main"

import os
import threading
import time

def Evenfactor(No):
    Sum = 0
    for i in range(1,No,1):
        if(No % i == 0):
            if(i % 2 == 0):
                Sum = Sum + i
            print("Addition Even factor is : ",Sum)

def Oddfactor(No):
    Sum = 0
    for i in range(1,No,1):
        if(No % i == 0):
            if(i % 2 != 0):
                Sum = Sum + i
            print("Addition Odd factor is : ",Sum)

def main():
    print("Enter the number")
    Value = int(input())
    
    T1 = threading.Thread(target = Evenfactor,args = (Value,))
    T2 = threading.Thread(target = Oddfactor,args = (Value,))
    
    T1.start()
    T2.start()
    
    T1.join()
    T2.join()

    print("Exit from main")


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",(end_time - start_time))