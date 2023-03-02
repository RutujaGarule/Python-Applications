print("accept number and print *")

def main():
    print("enter the number")
    No = int(input())
    for No in range(0,No,1):
        print("*",end = " ")
    
if __name__ == "__main__":
    main()