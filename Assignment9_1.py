# Accept filename and check that file exists in current directory or not

import os

def ChkFile(File_Name):
    if(os.path.exists(File_Name)):
        print("File is present in current directory")
    else:
        print("There is no file")

def main():
    print("Enter the name of file")
    File = input()
  
    ChkFile(File)

if __name__ == "__main__":
    main()