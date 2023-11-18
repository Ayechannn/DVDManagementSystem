import csv
from dvd import DVD
from customer import Customer
from binarytree import CustomerBinaryTree
from linkedlist import LinkedList
from colorama import init
from termcolor import colored

dvdList = LinkedList()
file = open("dvd.csv", "r")
for line in file:
    data = line.rstrip().split(",")
    newDVD = DVD(data[0], data[1], data[2], data[3], data[4], data[5])
    dvdList.insert_DVD(newDVD)
file.close()


cusList = CustomerBinaryTree()
inFile = open("customer.csv", "r")
for line in inFile:
    data = line.rstrip().split(",")
    dvd1 = dvdList.search_DVD(data[3])
    dvd2 = dvdList.search_DVD(data[4])
    dvd3 = dvdList.search_DVD(data[5])
    rentedDVD = [dvd1, dvd2, dvd3]
    newCustomer = Customer(data[0], data[1], data[2], rentedDVD)
    cusList.insert(newCustomer)
inFile.close()


# Adding a new customer
def addCustomer():
    first_name = input("Enter the first name : ")
    last_name = input("Enter the last name : ")
    account_no = input("Enter the account number : ")

    dvd1Title = input("Enter the title of rented DVD 1 : ")
    dvd1 = dvdList.search_DVD(dvd1Title)
    dvd2Title = input("Enter the title of rented DVD 2 : ")
    dvd2 = dvdList.search_DVD(dvd2Title)
    dvd3Title = input("Enter the title of rented DVD 3 : ")
    dvd3 = dvdList.search_DVD(dvd3Title)
    rentedDVD = [dvd1, dvd2, dvd3]
    newCustomer = Customer(first_name, last_name, account_no, rentedDVD)
    cusList.insert(newCustomer)
    print("New customer is successfully added \n")
    print(newCustomer)


def searchCustomer():
    customerId = input("Enter the customer account number to search(Axxx) : ")
    cus = cusList.search(customerId)
    if cus:
        print("\n The customer exists")
        print(cus)
    else:
        print("\n The customer does not exist")


def searchDVD():
    dvdTitle = input("Enter the title of the DVD to search : ")
    dvd = dvdList.search_DVD(dvdTitle)
    if dvd:
        print("\n The DVD exists")
        print(dvd)
    else:
        print("\n The DVD does not exist")


def updateCustomer():
    customerId = input("Enter the customer account number to update (Axxx) : ")
    cus = cusList.search(customerId)
    if cus:
        while True:
            print('\n Update the customer details')
            print("-----------------------------------------")
            print('1. Update the first name')
            print('2. Update the last name')
            print('3. Update the account number')
            print('4. Update the rented DVD lists')
            print('5. Exit \n')

            ans = int(input('\n What would you like to do? '))

            if ans == 1:
                fName = input('Enter the updated first name : ')
                cus.set_fName(fName)
                print('The first name has been updated')
            elif ans == 2:
                lName = input('Enter the updated last name : ')
                cus.set_lName(lName)
                print('The last name has been updated')
            elif ans == 3:
                acc_no = input('Enter the updated account no : ')
                cus.set_accountNo(acc_no)
                print('The account no has been updated')
            elif ans == 4:
                rent_dvd = input('Enter the updated number of rented DVD : ')
                cus.set_dvdList(rent_dvd)
                print('The number of rented DVD has been updated')
            elif ans == 5:
                print('The updated customer detail')
                print("-------------------------------------")
                print(cus)
                adminMenu()
            else:
                print('Wrong Option. Please choose valid one')
    else:
        print('The customer does not exist')


def addingDVD():
    title = input('Enter the title of the movie : ')
    cast = input('Enter the name of the cast : ')
    producer = input('Enter the name of the producer : ')
    director = input('Enter the name of the director : ')
    pro_company = input('Enter the production company : ')
    no_of_copy = int(input('Enter the number of copies : '))
    newDVD = DVD(title, cast, producer, director, pro_company, no_of_copy)
    dvdList.insert_DVD(newDVD)
    print('New DVD is successfully added \n')
    print(newDVD)


def removeDVD():
    dvd = input('Enter the title of the DVD that you want to remove : ')
    temp = dvdList.search_DVD(dvd)
    if temp:
        dvdList.remove_DVD(temp)
        print('\n The DVD that you want to remove is found in the store')
        print('DVD is successfully removed \n')
        print(dvd)
    else:
        print('DVD that you want to remove does not exist in the store \n')


def updateDVD():
    title = input('Enter the DVD title : ')
    dvd = dvdList.search_DVD(title)
    if dvd:
        while True:
            print('\n Update the DVD details')
            print("------------------------------------")
            print('1. Update the title of the DVD')
            print('2. Update the name of the cast')
            print('3. Update the name of the producer')
            print('4. Update the name of the director')
            print('5. Update the name of the production company')
            print('6. Update the number of the copies')
            print('7. Exit \n')

            ans = int(input('\n What would you like to do? '))
            if ans == 1:
                new_title = input('\n Enter the new title : ')
                dvd.set_movie_name(new_title)
                print('The DVD title has been updated')
            elif ans == 2:
                new_cast = input('\n Enter the new name of the cast : ')
                dvd.set_cast(new_cast)
                print('The name of the cast has been updated : ')
            elif ans == 3:
                new_producer = input('\n Enter the new name of the producer : ')
                dvd.set_producer(new_producer)
                print('The name of the producer has been updated : ')
            elif ans == 4:
                new_director = input('\n Enter the new name of the director : ')
                dvd.set_director(new_director)
                print('The name of the director has been updated')
            elif ans == 5:
                new_pro_company = input('\n Enter the new name of the production company : ')
                dvd.set_production_compay(new_pro_company)
                print('The name of the production company has been updated')
            elif ans == 6:
                new_no = input('\n Enter the new number of the copy : ')
                dvd.set_no_of_copies(new_no)
                print('The number of copies(Stock) has been updated : ')
            elif ans == 7:
                print('The update DVD detail')
                print("----------------------------------")
                print(dvd)
                adminMenu()
            else:
                print('Wrong Option. Please choose valid one')
    else:
        print('The DVD that you want to update does not exist in the store')


def checkDVDExist():
    dvd_title = input('Enter the DVD name that you are looking for : ')
    dvd = dvdList.search_DVD(dvd_title)
    if dvd:
        print('\n The DVD you are looking for exists in the store.')
        print(dvd)
    else:
        print('\n The DVD you are looking for does not exist in the store.')


def checkDVDAvailable():
    title = input('Enter the name of the DVD you are looking for : ')
    dvd = dvdList.search_DVD(title)
    if dvd:
        if dvd.get_no_of_copies() > 0:
            print('\n The DVD is available to borrow.', dvd.get_movie_name())
        else:
            print('\n The DVD is out of stock right now')
    else:
        print('\n The DVD does not exist in the store')


def viewDetailDVD():
    title = input('Enter the DVD title you want to look in detail : ')
    dvd = dvdList.search_DVD(title)
    if dvd:
        print('The detail information of the DVD is : ')
        print(dvd)
    else:
        print('The DVD you are looking for does not exist in the store.')


def cusRentDVD():
    cus_id = input('Enter the customer account number : ')
    cus = cusList.search(cus_id)
    if cus:
        print('The Lists of the rented DVDs by the customer ')
        cus.printRentedDVD()
    else:
        print('The customer is not found \n')


# The Menu Option for admin of the DVD store
def adminMenu():
    while True:
        print('\n DVD store menu for admin')
        print("-------------------------------------------------------")
        print('1.  Register a new Customer')
        print('2.  View the lists of the all customers')
        print('3.  Search for the detail information of the customer')
        print('4.  Update the customer detail')
        print('5.  View all DVDs in the store')
        print('6.  Add new DVD to the store')
        print('7.  Search DVD')
        print('8.  Remove DVD from the store')
        print('9.  Update DVD detail')
        print('10. Update the number of stock to DVD')
        print('11. Back to Main Menu')
        print("------------------------------------------------------- \n")

        ans = input('Choose One Option : ')

        if ans == "1":
            addCustomer()
        elif ans == "2":
            print('The Lists of all customers details')
            print("------------------------------------------------")
            cusList.printBinarytree()
        elif ans == "3":
            searchCustomer()
        elif ans == "4":
            updateCustomer()
        elif ans == "5":
            print('The Lists of all DVDs')
            print("---------------------------------------")
            dvdList.print()
        elif ans == "6":
            num = int(input('How many DVDs do you want to add? '))
            for i in range(num):
                print("Adding DVD : ", i + 1)
                addingDVD()
                print()
        elif ans == "7":
            searchDVD()
        elif ans == "8":
            removeDVD()
        elif ans == "9":
            updateDVD()
        elif ans == "10":
            title = input('Enter the DVD title to update the stock : ')
            dvd = dvdList.search_DVD(title)
            if dvd:
                new = int(input('Enter the number that u want to add : '))
                dvd.updateStock(new)
            else:
                print('The DVD you want to update does not exist', 'red')
        elif ans == "11":
            main()
        else:
            print('Wrong option! Please choose the valid one')


def customerMenu():
    while True:
        print('\n Welcome to the store : Customer Panel')
        print("-----------------------------------------------------------")
        print('1. Check if the DVD exists or not in the store')
        print('2. Check if the DVD is available for renting')
        print('3. Check out the DVD(Rent)')
        print('4. Check In the DVD(Return)')
        print('5. List all of the titles of the DVD')
        print('6. Show all the detail information of the DVD')
        print('7. Print a list of the DVDs that are rented by a customer')
        print('8. Back to main menu')

        answer = int(input('\n What would you like to do? '))

        if answer == 1:
            checkDVDExist()
        elif answer == 2:
            checkDVDAvailable()
        elif answer == 3:
            name = input('Enter the DVD title to check out : ')
            dvd = dvdList.search_DVD(name)
            if dvd:
                dvd.checkout_dvd()
            else:
                print('The DVD does not exist in the store.')
        elif answer == 4:
            title = input('Enter the DVD title to check in : ')
            dvd = dvdList.search_DVD(title)
            if dvd:
                dvd.checkin_dvd()
            else:
                print('The DVD does not exist in the store.')
        elif answer == 5:
            print('\n The Lists of all the DVDs in the store')
            print("--------------------------------------------------")
            dvdList.print()
        elif answer == 6:
            viewDetailDVD()
        elif answer == 7:
            cusRentDVD()
        elif answer == 8:
            main()
        else:
            print('Wrong option! Please choose the valid one')


def main():
    while True:
        print('\n ----------Welcome to our DVD Store----------')
        print("---------------------------------------------")
        print('1. Customer Menu')
        print('2. Admin Menu')
        print('3. Exit')
        print("--------------------------------------------- \n")

        answer = input('What would you like to do? Choose one option : ')
        if answer == "1":
            customerMenu()
        elif answer == "2":
            adminMenu()
        elif answer == "3":
            quit()
        else:
            print('Wrong Option. Please choose a valid one')


if __name__ == '__main__':
    main()
