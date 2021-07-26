# storing information of employees in a list such as their name, age, position, and the year they started working.
kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]
# class named dog is defined 
class Dog:
    pass
    
#The properties that all Dog objects are defined in a method called .__init__().Every time a new Dog object is created __init__() initializes each new instance of the class.
# the Dog class is updated with an .__init__() method that creates .name and .age attributes:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
#self.name=name creates an attribute name,assigns to it value of  name parameter and self.age=age creates an attribute age,assigns to it the value of age parameter.
#the following Dog class has a class attribute called species with the value "Canis familiaris":
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
#This creates two new Dog instances—one for a nine-year-old dog named Buddy and one for a four-year-old dog named Miles.        
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)   

#In this example,we change the.age attribute of the buddy object to 10. Then we change the .species attribute of the miles object to "Felis silvestris"
buddy.age = 10
miles.species = "Felis silvestris"

# Here theInstance methods are functions that are defined inside a class and can only be called from an instance of that class.Here dog class has 2 instances
#.description() returns a string displaying the name and age of the dog.
#.speak() has one parameter called sound and returns a string containing the dog’s name and the sound the dog makes.
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    
 #changing the name of the Dog class’s .description() method to .__str__():
class Dog:
    # Leave other parts of Dog class as-is

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"
 
#modifying the Dog class by adding a .breed attribute:
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
#breed mentioned in the following      
miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")     
#create a child class for each of the three breeds mentioned above: Jack Russell Terrier, Dachshund, and Bulldog
#to create a child class,we create new class with its own name and then put the name of the parent class in parentheses.
#Add following to the dog.py file to create three new child classes of the Dog class:

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
      
 class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass     
      
# instantiating some dogs of specific breeds 
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
#Instances of child classes inherit all of the attributes and methods of the parent class:
miles.species
'Canis familiaris'
buddy.name
'Buddy'
print(jack)
Jack is 3 years old
jim.speak("Woof")
'Jim says Woof'

#to determine if miles is also an instance of the Dog class
isinstance(miles, Dog)

#to override a method defined on the parent class,we define a method with the same name on the child class. Here’s it looks like for the JackRussellTerrier class:
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
#Updating dog.py with the new JackRussellTerrier class       
miles = JackRussellTerrier("Miles", 4)
miles.speak()
