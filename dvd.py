
# To keep the list of DVD for DVD store

class DVD:

    def __init__(self, movie_name, cast, producer, director, production_company, no_of_copies):
        self.__movie_name = movie_name
        self.__cast = cast
        self.__producer = producer
        self.__director = director
        self.__production_company = production_company
        self.__no_of_copies = int(no_of_copies)

    # get and set method for DVD class's attributes

    def set_movie_name(self, movie_name):
        self.__movie_name = movie_name

    def get_movie_name(self):
        return self.__movie_name

    def set_cast(self, cast):
        self.__cast = cast

    def get_cast(self):
        return self.__cast

    def set_producer(self, producer):
        self.__producer = producer

    def get_producer(self):
        return self.__producer

    def set_director(self, director):
        self.__director = director

    def get_director(self):
        return self.__director

    def set_production_company(self, production_company):
        self.__production_company = production_company

    def get_production_company(self):
        return self.__production_company

    def set_no_of_copies(self, no_of_copies):
        self.__no_of_copies = no_of_copies

    def get_no_of_copies(self):
        return self.__no_of_copies

    def __str__(self):
        output1 = "\nName of the DVD : " + self.__movie_name + "\n"
        output2 = "Name of the stars : " + self.__cast + "\n"
        output3 = "Name of the producer : " + self.__producer + "\n"
        output4 = "Name of the director : " + self.__director + "\n"
        output5 = "Name of the production company : " + self.__production_company + "\n"
        output6 = "Number of the copies in the store : " + str(self.__no_of_copies) + "\n"
        return output1 + output2 + output3 + output4 + output5 + output6

    def checkin_dvd(self):
        self.__no_of_copies += 1
        print("\n Successfully checked-in DVD ")
        print("The updated number of copies is : ", self.__no_of_copies)

    def checkout_dvd(self):
        if self.__no_of_copies > 0:
            self.__no_of_copies -= 1
            print("\n Successfully checked-out DVD ")
            print("The updated number of copies is : ", self.__no_of_copies)
        else:
            print("\n This DVD is out of stock right now")

    def updateStock(self, new):
        self.__no_of_copies += new
        print("The updated number of book is : ", self.__no_of_copies)
