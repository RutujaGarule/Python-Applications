
def main():
    print("Enter howmany elements you want to store")
    iSize = int(input())
    
    Input = []
    print("Enter the elements")
    for i in range(0,iSize,1):
        Value = int(input())
        Input.append(Value)
        
    print("Elements from the list is :",Input)    
    

if __name__ == "__main__":
    main()