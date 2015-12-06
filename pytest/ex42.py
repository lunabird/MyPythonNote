#-*- coding:utf-8 -*-
##Animal is-a object.
class Animal(object):
	pass

##Dog is-a Animal.
class Dog(Animal):

	def __init__(self, name):
		##
		self.name = name

##Cat is-a Animal.
class Cat(Animal):
	def __init__(self, name):
		##
		self.name = name

##Person is-a object.
class Person(object):
	def __init__(self, name):
		self.name = name
		##Peron has-a pet of some kind
		self.pet = None

##Employee is-a person.
class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary

class Fish(object):
	pass
class Salmon(Fish):
	pass
class Halibut(Fish):
	pass


rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover


flipper = Fish()

crouse = Salmon()

harry = Halibut()