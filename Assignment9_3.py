# Accept filename from user and create new file names as Demo.txt
# copy all contents from existing file into new file
# Accept filename through command line arguments

import os
import shutil
from sys import *

def CopyFile(File1,File2):  
    shutil.copyfile(File1,File2)
    Data = open(File1,"r")
    print(Data)

def main():
    
    print("This application is used to copy contents of one file into another")
    print("Enter name of another file")
    File1 = input()
    fd = open(File1,"r")
    
    if(len(argv) < 2):
        print("Insufficient arguments")
        exit()
   
    CopyFile(fd,argv[1])

if __name__ == "__main__":
    main()