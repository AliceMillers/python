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

#shoppincart
class ShoppingCart(object):
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print (product + " added.")
        else:
            print (product + " is already in the cart.")

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print (product + " removed.")
        else:
            print (product + " is not in the cart.")
my_cart = ShoppingCart("Patrick")
my_cart.add_item("Milk", 15.9)
my_cart.add_item("Bread", 6)
my_cart.add_item("Vodka", 22.5)
my_cart.remove_item("Vodka")

#about job
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)
milton = PartTimeEmployee("Jack")
print (milton.full_time_wage)

#triangle function
class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    number_of_sides = 3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False