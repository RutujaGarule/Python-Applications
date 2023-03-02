print("Pattern printing")

def Pattern(No):
    for i in range(0,No,1):
        for j in range(1,No+1,1):
            print("*",end = "   ")
        print()    

def main():
    print("enter the number")
    i = int(input())
    
    Pattern(i)



if __name__ == "__main__":
    main()