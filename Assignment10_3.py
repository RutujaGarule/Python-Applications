# Design automation script which accept two directory names
# copy all files from first directoy into second directory
# Second directory should be created at run time

import os
import shutil
from sys import*

def CopyFiles(dir1,dir2):
    flag = os.path.isabs(dir1)
    if flag == False:
        path = os.path.abspath(dir1)
        
    exists = os.path.isdir(path)
        
    if exists:
        for folder,subfolder,filename in os.walk(path):
            for file in filename:
                shutil.copytree(dir1,dir2)
                
    else:
        print("Invalid path")
                

def main():
    print("-----Automation Script-----")
    print("Application Name is : ",argv[0])
        
    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used to copy all files from first directory into second directory")
        exit()
        
    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Application_Name Directory_1 Directory_2")
        exit()
     
    if(len(argv) != 3):
        print("Error : Invalid argumnets")
        exit()
    try:    
        CopyFiles(argv[1],argv[2])
       
    except Exception as E:
        print("Error :",E)
        
if __name__ == "__main__":
    main()