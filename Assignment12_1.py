# Design automation script which display information of running process as its name ,PID,Username.


from sys import *
import psutil

def ProcessInfo():
    list = []
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            list.append(pinfo)
            
        except(psuti.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
        
    return list


def main():
    print("-----Automation Script to display Information of running process-----")
    print("Application Name : ",argv[0])
       
    Arr = ProcessInfo()
    for process in Arr:
        print(process)


if __name__ == "__main__":
    main()