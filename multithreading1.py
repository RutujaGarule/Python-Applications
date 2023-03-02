import time
import threading

def DisplayEven(No):
    for i in range(1,No,1):
        if(i%2 == 0):
            print("Even number : ",i)    


def DisplayOdd(No):
    for i in range(1,No,1):
        if(i%2 != 0):
            print("Odd number : ",i)    



def main():
    print("Demonstration of parallel progeamming using multiple threads")
    
    Number = 2000
    
    P1 = threading.Thread(target = DisplayEven, args = (Number,))
    P2 = threading.Thread(target = DisplayOdd, args = (Number,))
    
    P1.start()
    P2.start()
    
    P1.join()
    P1.join()
    
    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)