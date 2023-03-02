# Design automation script which accept two directory names nad one file extension
# copy all files with specified extension from first directoy into second directory
# Second directory should be created at run time

import os
import shutil
from sys import*

def CopyFiles(dir1,dir2,Ext):
    flag = os.path.isabs(dir1)
    if flag == False:
        dir1 = os.path.abspath(dir1)
        
    exists = os.path.isdir(dir1)
        
    if exists:
        for folder,subfolder,filename in os.walk(dir1):
            for file in filename:
                if file.endswith(Ext):
                    shutil.copy(dir1,dir2)
                
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
     
    if(len(argv) != 4):
        print("Error : Invalid argumnets")
        exit()
    try:    
        CopyFiles(argv[1],argv[2],argv[3])
       
    except Exception as E:
        print("Error :",E)
        
if __name__ == "__main__":
    main()