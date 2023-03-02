# pattern printing

def Pattern(No):
    for i in range(0,No,1):
        for j in range(0,(No-i),1):
            print("*",end = "   ")
        print()



def main():
    print("Enter the number")
    Value = int(input())
    
    Pattern(Value)



if __name__ == "__main__":
    main()