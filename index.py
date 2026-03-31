class Pet:
    name=None
    animal_type=None
    age=0
    def __init__(self,n,t,a):
        self.name=n 
        self.type=t 
        self.age=a 
    def setName(self,n):
        self.name=n 
    def setType(self,t):
        self.type=t 
    def setAge(self,t):
        self.age=a 
    def getName(self):
        return name
    def getType(self):
        return animal_type
    def getAge(self):
        return age


n=input("Enter the name of your pet: ")
t=input("Enter the animal_type: ")
a=input("Enter the age: ")
pl=Pet(n, t, a)