# recurssive program to display below pattern
# 5
# 5    4   3   2   1

def Pattern(No):
    if(No > 0):
        print(No,end = " ")
        No = No -1
        Pattern(No)


def main():
    print("Enter number")
    Value = int(input())
    
    Pattern(Value)


if __name__ == "__main__":
    main()