# python application contains two threads as evenlist and oddlist .Both threads accept list of integers as parameters
# Evenlist thread will display addtion of even numbers and oddlist will display addition of odd elements
# After execution of both thread gets completed main thread will display "exit from main"

import os
import threading
import time

def Evenlist(Arr):
    Sum = 0;
    for i in range(0,len(Arr),1):
        if(Arr[i] % 2 == 0):
            Sum = Sum + Arr[i]
        print("Addition of even numbers is : ",Sum)
        

def Oddlist(Arr):
    Sum = 0;
    for i in range(0,len(Arr),1):
        if(Arr[i] % 2 != 0):
            Sum = Sum + Arr[i]
            print("Addition of even numbers is : ",Sum)

def main():
    Input = []
    print("Enter size of elements")
    Size = int(input())
    
    print("Enter the elements")
    for i in range(0,Size,1):
        Value = int(input())
        Input.append(Value)

    T1 = threading.Thread(target = Evenlist,args = (Input,))
    T2 = threading.Thread(target = Oddlist,args = (Input,))
    
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