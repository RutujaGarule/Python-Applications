# Design automation script which accept directory name and two file extension from user
# Rename all files with first file extension with the second file extension

import os 
from sys import *

def Change_Extension(Dir_Name,Ext1,Ext2):
    print("Inside Change_Extension Method")
    
    for Folder,subfolder,filename in os.walk(Dir_Name):
        for files in filename:
            split = os.path.splitext(files)
            if(split[1] == Ext1):
                Name = os.path.join(split[0]+Ext2)
               
                print(Name)

def main():
    print("Automation Script to change the extension of files")
    
    if(len(argv) < 4):
        print("Insufficient Arguments")
        exit()
        
    if((argv[1] == "H") or (argv[1] == "h")):
        print("This scrit is used to change extension of files")
        exit()
        
    if((argv[1] == "U") or (argv[1] == "u")):
        print("Usage : Directory_Name Extension1,Extension2")
        exit()
        
    Change_Extension(argv[1],argv[2],argv[3])

if __name__ == "__main__":
    main()