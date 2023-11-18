
# To keep the list of customer
from dvd import DVD


class Customer:

    def __init__(self, fName, lName, accountNo, dvdList=None):
        self.__fName = fName
        self.__lName = lName
        self.__accountNo =accountNo
        self.__dvdList = dvdList

    # set and get methods for Customer class's attributes
    
    def set_fName(self, fName):
        self.__fName = fName

    def get_fName(self):
        return self.__fName

    def set_lName(self, lName):
        self.__lName = lName

    def get_lName(self):
        return self.__lName

    def set_accountNo(self, accountNo):
        self.__accountNo = accountNo

    def get_accountNo(self):
        return self.__accountNo

    def set_dvdList(self, dvdList):
        self.__dvdList = dvdList

    def get_dvdList(self):
        return self.__dvdList

    def rentingDVD(self, dvd):
        self.__dvdList.append(dvd)

    def returnRentedDVD(self, dvd):
        self.__dvdList.pop(dvd)

    def __eq__(self, other):    # equal operator
        return self.__accountNo == other.__accountNo

    def __lt__(self, other):    # less than operator
        return self.__accountNo < other.__accountNo

    def __gt__(self, other):    # greater than operator
        return self.__accountNo > other.__accountNo

    def __le__(self, other):    # less than, equal operator
        return self.__accountNo <= other.__accountNo

    def __ge__(self, other):    # greater than, equal operator
        return self.__accountNo >= other.__accountNo

    def __str__(self):
        output1 = "Name : " + self.__fName + " " + self.__lName + "\n"
        output2 = "Account Number : " + self.__accountNo + "\n"
        output3 = "Rented DVD 1 : " + self.__dvdList[0].__str__() + "\nRented DVD 2 : " + self.__dvdList[1].__str__() \
                  + "\nRented DVD 3 : " + self.__dvdList[2].__str__()
        return output1 + output2 + output3

    def printRentedDVD(self):
        print("List of rented DVDs \n")
        print("----------------------")
        output = "Rented DVD 1 : " + self.__dvdList[0].__str__() + "\n Rented DVD 2 : " + self.__dvdList[1].__str__() \
                  + "\n Rented DVD 3 : " + self.__dvdList[2].__str__()
        print(output)

        