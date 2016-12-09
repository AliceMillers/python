class Person(object):
    def __init__(self, name, age):
        age = self.age
        name = self.name
    def say_hello(self):
        return "Hi, I'm %s. My age is %s." % ( self.age, self.name)
  
