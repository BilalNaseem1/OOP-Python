class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary



if __name__ == "__main__":
    oPerson1 = Person("Bilal", 100000)
    print(oPerson1.name)
    print(oPerson1.salary)