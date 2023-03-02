# Design automation script which accept name of process
# and display information of that process if it is running


from sys import *
import psutil

def ProcessInfo(Name):
    
    for proc in psutil.process_iter():
        try:
            if(Name.lower() in proc.name().lower()):
                pinfo = proc.as_dict(attrs = ['pid','name','username'])
                return pinfo
                
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
            
    print("No such process running")


def main():
    print("-----Automation Script to display Information of process if it is running-----")
    print("Application Name : ",argv[0])
    
    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()
        
    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Application_Name Name_of_Process")
        exit()
        
    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used to dislay information of process if it is running")
        exit()
       
    Arr = ProcessInfo(argv[1])
    print(Arr)


if __name__ == "__main__":
    main()