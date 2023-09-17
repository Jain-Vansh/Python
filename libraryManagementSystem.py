class Library:
    bookName = ["Uncharted-1","God of War","GTA-5","Spiderman","Red Dead Redemption"]
    bookCount = len(bookName)

    def showBooks(self):
        print("Here are all the available books - \n",self.bookName)

    def addBook(self,book):
        self.bookName.append(book)
        self.bookCount = len(self.bookName)
        print(f"Book '{book}' has been successfully added.")
        print(f"Total Books available are {self.bookCount}")

    def issueBook(self):
        self.showBooks()
        issue = input("Please enter book name you want to issue: ")
        if(issue not in self.bookName):
            print("Sorry this book is unavailable at the moment")
        else:
            print(f"Book '{issue}' has been successfully issued.")
            self.bookName.remove(issue)
            self.bookCount = len(self.bookName)



lib = Library()
lib.showBooks()
lib.addBook("Call of Duty")
lib.issueBook()
