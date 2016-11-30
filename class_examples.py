class Animal(object):
    def __init__(self, name):
        self.name = name
zebra = Animal("Jeffrey")
print (zebra.name)

# Class definition
class Animal(object):
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.name, giraffe.age, giraffe.is_hungry)
print (panda.name, panda.age, panda.is_hungry)

#A Methodical Approach
class Animal(object):
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print (self.name)
        print (self.age)
hippo = Animal("Ostin", 7)
print (hippo.name, hippo.age)