print("display first 10 even numbers")

def main():
    print("enter the number")
    No = int(input())
    for No in range(2,No,2):
        print(No)
    
if __name__ == "__main__":
    main()