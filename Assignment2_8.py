print("pattern printing")

def Pattern(Val):
    for i in range(1,Val+1,1):
        for j in range(1,i+1,1):
            print(j,end = " ") 
        print()
    
    
def main():
    print("Enter the number")
    No = int(input())
    
    Pattern(No)

if __name__ == "__main__":
    main()