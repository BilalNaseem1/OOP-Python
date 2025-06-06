class Person:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        
    @property        
    def salary(self):
        return self.__salary

    @property
    def name(self):
        return self.__name
    
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
        return self.__salary

    @name.setter
    def name(self, name):
        self.__name = name
        return self.__name
    

if __name__ == "__main__":
    oPerson = Person("Bilal", 90)

    print(oPerson.salary)  
    oPerson.salary = 100    
    print(oPerson.salary)    

    print(oPerson.name)        
    oPerson.name = "Hassan"   
    print(oPerson.name)        
