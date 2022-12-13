from scripts import Book, Shelf, basicUser, librarianUser
import logging
import openpyxl

#_______________Defining a shelf instance in the beginning_________

shelf = Shelf()

#Changing logging configurations
logging.basicConfig(filename = 'Issue and Return Logs.log', level = logging.DEBUG) 


#______________________Interface__________________
#First Screen
while True:
    print(
    '''
    Please Log In to Your Account
    Type the number corresponding to the option that you wish to choose :
    1. Basic Account
    2. Librarian Account 
    3. Exit
        '''
    )

    #Making sure a valid choice is input
    userAccountChoice = 0
    while userAccountChoice not in [1,2,3]:
        userAccountChoice = int(input('Enter Your Choice : '))
        if userAccountChoice not in [1,2,3]:
            print('Enter a valid number')

    #IF user enters 3, instantly program closes
    if userAccountChoice == 3:
        break

    #Asking the user for his details for the definition of the user
    username = input('Enter Your Name : ')
    userid = input('Enter Your ID : ')

    #Defining the user and his access rights
    if userAccountChoice == 1:
        user = basicUser(username, userid)
    elif userAccountChoice == 2:
        #TBA - Login Mechanism
        user = librarianUser(username, userid)

    while True:
        if user.hasAdminAccess :
            print ('______________ADMIN ACCOUNT____________')
            print(
                '''
                Shelf Features
                1. Show The Catalog
                2. Add Book
                3. Remove Book
                4. Get Books Count
                5. Populate The Shelf
                6. Edit Book Details
                7. Back
                '''
            )

            #Making sure a valid choice is input
            userFunctionChoice = 0
            while userFunctionChoice not in list(range(1, 8)):
                userFunctionChoice = int(input('Enter Your Choice : '))
                if userAccountChoice not in list(range(1, 8)):
                    print('Enter a valid number')

            if userFunctionChoice == 1:
                shelf.showCatalog()

            elif userFunctionChoice == 2:
                bookName = input('Enter the book name : ')
                bookISBN = input('Enter the ISBN of the book : ')
                bookAuthor = input('Enter the Author of the book : ')
                book = Book(bookName, bookISBN, bookAuthor)
                shelf.addBook(book)

            elif userFunctionChoice == 3:
                if shelf.isEmpty() :
                    print("The Shelf is already empty.\n Hence You can't remove anything from the shelf")
                else:
                    userRemovalBookChoice = 0
                    userRemovalBookChoice = shelf.chooseBook(userRemovalBookChoice, 'Enter The Book To Remove : ')
                    shelf.removeBook(userRemovalBookChoice - 1)

            elif userFunctionChoice == 4:
                print(shelf.booksCount)

            elif userFunctionChoice == 5:
                shelf.populateBooks()
                print('\nBooks were successfully added to the shelf\n')

            elif userFunctionChoice == 6:
                userChangeBookDetailsChoice = 0
                userChangeBookDetailsChoice = shelf.chooseBook(userChangeBookDetailsChoice, 'Enter the Book To Change the details of : ')

                chosenBook = shelf.array[userChangeBookDetailsChoice - 1]

                print(
                    '''
                    Which detail do you want to change?
                    1. Title
                    2. ISBN
                    3. Author
                    '''
                )
                userDetailsChoice = int(input('Enter the detail you want to change of the chosen book : '))

                if userDetailsChoice == 1:
                    newBookTitle = input('Enter the new name for {} : '.format(chosenBook.name))
                    chosenBook.name = newBookTitle
                
                elif userDetailsChoice == 2:
                    newisbn = input('Enter the new ISBN for {} (Current ISBN : {}) : '.format(chosenBook.name, chosenBook.isbn))
                    chosenBook.isbn = newisbn

                elif userDetailsChoice == 3:
                    newAuthor = input('Enter thenew Author for {} (Current Author : {}) : '.format(chosenBook.name, chosenBook.author))
                    chosenBook.author = newAuthor

                #Updating the shelf with the new book instance
                shelf.array[userChangeBookDetailsChoice - 1] = chosenBook

            else :
                break

        else:
            print ('______________BASIC ACCOUNT____________')
            print(
                '''
                1. Issue a book
                2. Return a book
                3. Reserve a book
                4. Back
                '''
            )

            #Making sure a valid choice is input
            userFunctionChoice = 0
            while userFunctionChoice not in [1,2,3,4]:
                userFunctionChoice = int(input('Enter Your Choice : '))
                if userAccountChoice not in [1,2,3,4]:
                    print('Enter a valid number')

            if userFunctionChoice == 1:
                # Testing the book borrowing
                #book.borrowBook(user)
                if user.hasBook:
                    print("You can't issue a new book as you already have borrowed - '{}'".format(user.bookHeld.name))
        
                elif shelf.isEmpty():
                    shelf.showCatalog()
        
                else:
                    print('List of the available books \n\n')
                    userBookBorrowChoice = 0
                    userBookBorrowChoice = shelf.chooseBook(userBookBorrowChoice, 'Enter the Book you want to borrow : ')
                    chosenBook = shelf.array[userBookBorrowChoice - 1]

                    #Removing the borrowed book from the shelf
                    shelf.removeBook(userBookBorrowChoice - 1)
                    print('\nRemoved {} from the shelf.\n'.format(chosenBook.name))
                    
                    #Adding the book to the user
                    chosenBook.borrowBook(user)
                    print('{} has successfully borrowed {}.'.format(username, chosenBook.name))

                    #Logging the issue of the book
                    logging.debug('Removed {} from the shelf.'.format(chosenBook.name))
                    logging.debug('{} has successfully borrowed {}.'.format(username, chosenBook.name))

            elif userFunctionChoice == 2:
                if user.hasBook:
                    bookHeldByUser = user.bookHeld
                    
                    #Returning the book method is used 
                    bookHeldByUser.returnBook(user)
                    print('\n{} has successfully returned {}.\n'.format(username, bookHeldByUser.name))

                    #Adding the returned book to the shelf
                    shelf.addBook(bookHeldByUser)
                    print('Added {} to the shelf.\n'.format(bookHeldByUser.name))

                    #Logging the return of the book
                    logging.debug('{} has successfully returned {}.\n'.format(username, bookHeldByUser.name))
                    logging.debug('Added {} to the shelf.\n'.format(bookHeldByUser.name))

            elif userFunctionChoice == 3 :
                userBookReserveChoice = 0
                userBookReserveChoice = shelf.chooseBook(userBookReserveChoice, 'Enter The Book you wish to reserve : ')

                chosenBook = shelf.array[userBookReserveChoice - 1]
                #Invoking the reserving function
                shelf.array[userBookReserveChoice - 1].reserveBook(user)
                print('{} has successfully reserved {}'.format(username, chosenBook.name))
        

            elif userFunctionChoice == 4 :
                break
                    
                


                    

                    


            


    

