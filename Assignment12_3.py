# Design automation script which accept directory name from user
# and create log file in that directory which contains information of running processes as its name,PID,Username.

import os
from sys import *
import psutil
import time

def ProcessInfo(dir):
    list = []

    if not os.path.exists(dir):
        try:
            os.mkdir(dir)
        except:
            pass
            
    log_path = os.path.join(dir,"MarvellousLog%s.log"%(time.ctime()))
    f = open(log_path,'w')
    f.write("Process Logger "+time.ctime() + "\n")
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            list.append(pinfo)
            
        except(psuti.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
        
    for element in list:
        f.write("%s\n" %element)


def main():
    print("-----Automation Script to create log file for Information of running process-----")
    print("Application Name : ",argv[0])
       
    
    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()
        
    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Application_Name Name_of_Directory")
        exit()
        
    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used to create log file of running process")
        exit()
    try:
        ProcessInfo(argv[1])
        
    except Exception as E:
        print("Error : ",E)
        

if __name__ == "__main__":
    main()