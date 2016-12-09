class Person(object):
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def say_hello(self):
        return "Hi, I'm %s. My age is %s." % ( self.age, self.name)
  
