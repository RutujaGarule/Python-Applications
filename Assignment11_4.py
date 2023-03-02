# Design automation script which accept name of directory and delete duplicate files from that directory .
# Write names of duplicate files into log file
# log.txt file shoild be created into current directory
# Display execution time required for the script


import hashlib
import os
from sys import*
import time


def hashfile(path,blocksize = 1024):
    file = open(path,'rb')
    hasher = hashlib.md5()
    buf = file.read(blocksize)
    
    while(len(buf) > 0):
        hasher.update(buf)
        buf = file.read(blocksize)
        
    file.close()
    return hasher.hexdigest()
    

def FindDuplicate(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
        
    Exists = os.path.isdir(path)
    
    dups = {}
    
    if Exists:
        for Folder,Subfolder,Filename in os.walk(path):
            print("Current folder is :",Folder)
            for file in Filename:
                path = os.path.join(Folder,file)
                hash_file = hashfile(path)
                if hash_file in dups:
                    dups[hash_file].append(path)
                else:
                    dups[hash_file] = [path]
        return dups
                
    else:
        print("Invalid path")


def printDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    
    if len(results) > 0:
        print("Duplicates found : ")
        print("The following files are identical :")
        
        iCnt = 0
        for result in results:
            for subresult in result:
                iCnt+=1
                if iCnt >= 2:
                    print(subresult)
                    print('')
            
    else:
        print("No duplicate found")


def DeleteFiles(dict1):
    results = list(filter(lambda x: len(x) > 1,dict1.values()))
    
    iCnt = 0
    
    if len(results) > 0:
        for result in results:
            for subresult in result:
                iCnt+=1
                if(iCnt >= 2):
                    os.remove(subresult)
            iCnt = 0
    else:
        print("No duplicate files found")
    

def main():
    print("-----Automation Script To delete duplicate files-----")
    print("Application Name : ",argv[0])
    
    if(len(argv) != 2):
        print("Error : Invalid arguments")
        exit()
        
    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used to delete name of duplicate files")
        exit()
        
    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Application_Name Directory_Name")
        exit()
    try:    
        startTime = time.time()
        Arr = FindDuplicate(argv[1])
        printDuplicate(Arr)
        DeleteFiles(Arr)
        endTime = time.time()
        
        print("Took %s seconds to evaluate"%(endTime - startTime))
        
    except Exception as E:
        print("Error:",E)
        


if __name__ == "__main__":
    main()