# Design automation script which accept directory name and file extension from user
# Display all files with that extension

import os 
from sys import *


def DirectoryFileSearch(Dir_Name,Extension):
    print("Inside DirectoryFileSearch method")
    print("Name of directory is {} and extension is {}".format(Dir_Name,Extension))
    
    for folder,subfolder,filename in os.walk(Dir_Name):
        for file in filename:
            if file.endswith(Extension):
                print(file)
            

def main():
    print("Automation Script DirectoryFile Search")
    
    if(len(argv) < 3):
        print("Insufficient Arguments")
        exit()
        
    if((argv[1] == "H") or (argv[1] == "h")):
        print("This scrit is used to search file in the directory")
        exit()
        
    if((argv[1] == "U") or (argv[1] == "u")):
        print("Usage : Directory_Name Extension")
        exit()
        
    DirectoryFileSearch(argv[1],argv[2])

if __name__ == "__main__":
    main()