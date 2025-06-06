class Person:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        
    def getSalary(self):
        return self.__salary


    def getName(self):
        return self.__name

    def setSalary(self, salary):
        self.__salary = salary
        return self.__salary

    def setName(self, name):
        self.nam__name = name
        return self.__name
    

if __name__ == "__main__":
    oPerson = Person("Bilal", 90)

    # print(oPerson.__salary) ## will raise error
    print(oPerson.getSalary())
    