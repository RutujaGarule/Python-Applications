


def main():
    Arr = list()
    
    print("Enter howmany elements you want to store?")
    size = int(input())
    
    print("please enter the values")
    
    for i in range(0,size,1):
        no = int(input())
        Arr.append(no)
        
        
    print(Arr)
    



if __name__ == "__main__":
    main()