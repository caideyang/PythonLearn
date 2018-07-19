class People:
    house_are = 100
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property
    def salary(self):
        return self.age * 1000

    @classmethod
    def go_school(cls):
        print("Hello",cls)
    @staticmethod
    def wash_body():
        print("This is a static method !")


people = People('caideyang',30)
print(people.age)
print(people.salary)
print(people.__dict__)
print(People.__dict__)
People.salary = 10000
print(People.__dict__)
people.go_school()
People.go_school()
People.wash_body()
people.wash_body()
