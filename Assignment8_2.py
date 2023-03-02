# recurssive program to display below pattern
# 5
# 1    2   3   4   5

def Pattern(No):
    if(No > 0):
        No = No -1
        Pattern(No)
        print(No+1,end = " ")

def main():
    print("Enter number")
    Value = int(input())
    
    Pattern(Value)


if __name__ == "__main__":
    main()