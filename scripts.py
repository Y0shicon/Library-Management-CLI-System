#from .script import populate
import openpyxl


class Book():
    def __init__(self, name, isbn, author, **kwargs):
        # all the necessary attributes and details of a book
        self.name = name
        self.isbn = isbn
        self.author = author
        self.holder = kwargs.get('Holder','None')
        self.reserver = kwargs.get('Reserver','None')
		
    def borrowBook(self, newHolder):
        self.holder = newHolder
        newHolder.borrowedBook(self)

    def returnBook(self, currentHolder):
        self.holder = 'None'
        currentHolder.returnedBook()

    def reserveBook(self, reserver):
        self.reserver = reserver

class Shelf():
    def __init__(self):
        self.array = []
        self.booksCount = 0

    def isEmpty(self):
        if self.array == []:
            return True
        return False

    def chooseBook(self, choice, inputStr):
        self.showCatalog()
        choice = 0
        while choice not in list(range(1,self.booksCount)):
            choice = int(input('\n' + inputStr))
            if choice not in list(range(1, self.booksCount)):
                print('Enter a valid number\n')
        return choice

    def showCatalog(self):
        if self.array == []:
            print('There no books in the catalogue. Please populate the shelf. \n')
        else:
            i = 0
            while i < len(self.array):
                print('{sno}. {title} by {author}    ISBN ---> {isbn} '.format(sno = i+1, title = self.array[i].name, author = self.array[i].author, isbn = self.array[i].isbn))
                i += 1

    def addBook(self, bookToAdd):
        self.array.append(bookToAdd)
        self.refreshBookCount()

    def removeBook(self, bookToRemoveIndex):
        self.array.pop(bookToRemoveIndex)
        self.refreshBookCount()

    def refreshBookCount(self):
        self.booksCount = len(self.array)

    def getBookCount(self):
        return self.booksCount
        # additional methods you can think of
		
    def populateBooks(self):
        wb = openpyxl.load_workbook('/Users/sukriti/Python/DVM Task/books.xlsx')

        sheet = wb.active
        rows = sheet.rows
        for row in rows:
            book = Book(row[0].value, row[1].value, row[2].value)
            self.array.append(book)
        
        self.refreshBookCount()

class basicUser():
    
    def __init__(self, name, _id, **kwargs):
        self.name = name
        self.id = _id
        self.hasAdminAccess = False
        self.bookHeld = kwargs.get('bookHeld', 'Nothing')
        self.refreshHasBook()

    def refreshHasBook (self):
        if self.bookHeld != 'Nothing':
            self.hasBook = True
        else:
            self.hasBook = False

    def returnedBook(self):
        self.bookHeld = 'Nothing'
        self.refreshHasBook()

    def borrowedBook(self, book):
        self.bookHeld = book
        self.refreshHasBook()

class librarianUser():

    def __init__(self, name, _id, **kwargs):
        self.name = name
        self.id = _id
        self.hasAdminAccess = True