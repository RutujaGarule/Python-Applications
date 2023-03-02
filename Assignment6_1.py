
class BookStore:

    NoOfBooks = 0
    
    def __init__(self):
        self.Name = ""
        self.Author = ""
        
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
    
    def Accept(self):
        print("Enter name of book")
        self.Name = input()
        print("Enter author of book")
        self.Author = input()
            
    
    def Display(self):
        print(self.Name,"by",self.Author,".", "No of books : ",BookStore.NoOfBooks)


def main():
    
    obj1 = BookStore()
    obj1.Accept()
    obj1.Display()
    
    obj2 = BookStore()
    obj2.Accept()
    obj2.Display()
    
    obj3 = BookStore()
    obj3.Accept()
    obj3.Display()



if __name__ == "__main__":
    main()