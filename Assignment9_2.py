# Accept filename and open that file and display contents of file on screen

import os

def Display(File_Name):
    if(os.path.exists(File_Name)):
        fd = open(File_Name,"r")
        Data = fd.read()
        print("Contents from file is : ")
        print(Data)
        
        fd.close()
        
    else:
        print("There is no such file")

def main():
    print("Enter the name of file")
    File = input()
  
    Display(File)

if __name__ == "__main__":
    main()