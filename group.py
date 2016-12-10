class Group(object):
    people = []
    def add_person(self, person):
        self.people.append(person)
    def say_hello(self):
        for i in self.people:
            print ("Hi, i'm %s. My age is %s." % (i.get_name(), i.get_age()))
