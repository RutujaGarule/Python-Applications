
import os
import multiprocessing

def Square(No):
    print("PID of worker process is {} for the input {}".format(os.getpid(),No))
    return (No*No)

def main():
    print("process ID of our application is :",os.getpid())
    
    Data = [1,2,3,4,5]
    Result = []
    
    pobj = multiprocessing.Pool()

    Result = pobj.map(Square,Data)
    
    print("result after square operation is :",Result)
    

if __name__ == "__main__":
    main()