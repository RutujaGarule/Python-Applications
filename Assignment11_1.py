# Design automation script which accept name of directory
# display checksum of all files

import hashlib
import os
from sys import*


def hashfile(path,blocksize = 1024):
    file = open(path,'rb')
    hasher = hashlib.md5()
    buf = file.read(blocksize)
    
    while(len(buf) > 0):
        hasher.update(buf)
        buf = file.read(blocksize)
        
    file.close()
    return hasher.hexdigest()



def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
        
    Exists = os.path.isdir(path)
    
    if Exists:
        for Folder,Subfolder,Filename in os.walk(path):
            print("Current folder is :",Folder)
            for file in Filename:
                path = os.path.join(Folder,file)
                hash_file = hashfile(path)
                print(path)
                print(hash_file)
                print('')
                
    else:
        print("Invalid path")


def main():
    print("-----Automation Script To Calculate Checksum of Files-----")
    print("Application Name : ",argv[0])
    
    if(len(argv) != 2):
        print("Error : Invalid arguments")
        exit()
        
    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used to calculate checksum of files in directory")
        exit()
        
    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Application_Name Directory_Name")
        exit()
    try:    
        DisplayChecksum(argv[1])
        
    except Exception:
        print("Error: invalid input")
        


if __name__ == "__main__":
    main()