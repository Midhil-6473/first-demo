# class Dog:
#     def bark(self):
#         print("bow bow")
        
# dog = Dog()
# dog.bark()     

# dog2 = Dog()
# dog2.bark()     

#-------------------------------------------------- 2nd example -----------------------------------------------------

# class Dog:
#     def __init__(self,name,breed,owner):   #__init__ is a constructor
#         self.name = name             #self refers to the current object
#         self.breed = breed
#         self.owner = owner
        
#     def bark(self):
#         print("bow bow")

# class owner:
#     def __init__(self,owner_name,owner_age,owner_address,owner_phone):
#         self.owner_name = owner_name
#         self.owner_age = owner_age
#         self.owner_address = owner_address
#         self.owner_phone = owner_phone

# owner1 = owner("john",34,"123 street","1234567890")
# dog1 = Dog("tommy","bulldog",owner1)       #dog1 and dog2 are objects of Dog class
# print(dog1.name,dog1.breed)
# dog1.bark()
# print(dog1.owner.owner_name)

# owner2 = owner("alice",28,"456 avenue","0987654321")
# dog2 = Dog("rocky","labrador",owner2)    
# print(dog2.name,dog2.breed)
# dog2.bark()    
# print(dog2.owner.owner_name)

#-------------------------------------------------- 3rd example -----------------------------------------------------

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print(f"Hello my name is {self.name}.I am {self.age} years old.")
       
# person1 = person("john",30)
# person1.greet() 

# person2 = person("alice",25)
# person2.greet()     

#-------------------------------------------------- 4th example -----------------------------------------------------

# class User:
#     def __init__(self,username,email):
#         self.username = username
#         self.email = email
    
#     def display_info(self,user):
#         print(f"Username: {user.username}, Email: {user.email}. Say, hello to {self.username}!")

# user1 =User("john_doe","john@example.com")
# user2 = User("jane_smith","jane@example.com")
# user1.display_info(user2)


# class User:
#     def __init__(self,username,email):
#         self.username = username
#         self.email = email
    
#     def display_info(self,user):
#         print(f"Username: {user.username}, Email: {user.email}. Say, hello to {self.username}!")

# user1 =User("john_doe","john@example.com")

# user1.username = "alice_wonder"                  #Modifying or updating attributes
# user1.email = "alice@example.com"

# print(user1.username,user1.email)

#-------------------------------------------------- 5th example -----------------------------------------------------
#Access modifiers: public, protected, private

# class User:
#     def __init__(self, username, email):
#         self.username = username           # Public attribute
#         self._email = email                # Protected attribute (convention)
#         self.__password = "secret"         # Private attribute (name mangled)

#     def _protected_method(self):         # Protected method
#         print("This is a protected method.")

#     def __private_method(self):          # Private method
#         print("This is a private method.")

# user1 = User("john_doe", "john@example.com")
# print(user1.username)                # Accessible
# print(user1._email)                  # Accessible (but conventionally avoided)
# # print(user1.__password)            # AttributeError: 'User' object has no attribute '__password'
# print(user1._User__password)         # Accessible via name mangling (not recommended)

# user1._protected_method()            # Callable (but conventionally avoided)
# # user1.__private_method()           # AttributeError
# user1._User__private_method()        # Callable via name mangling (not recommended)

#-------------------------------------------------- 6th example -----------------------------------------------------
#Getter and Setter methods

# In Python, getters and setters are methods used to access and modify private or protected attributes of a class.

# class Person:
#     def __init__(self, name, age):
#         self.__name = name          # Private attribute
#         self.__age = age            # Private attribute

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def get_age(self):
#         return self.__age

#     def set_age(self, age):
#         if age >= 0:
#             self.__age = age
#         else:
#             print("Age cannot be negative.")
            
# person1 = Person("John", 30)
# print(person1.get_name())  # Accessing name using getter
# print(person1.get_age())   # Accessing age using getter
# person1.set_name("Alice")  # Modifying name using setter
# person1.set_age(25)        # Modifying age using setter
# print(person1.get_name())
# print(person1.get_age())    
# person1.set_age(-5)
# print(person1.get_age()) 

#-------------------------------------------------- 7th example -----------------------------------------------------

# ...existing code...

#-------------------------------------------------- 6th example -----------------------------------------------------
#Getter and Setter methods

# In Python, a getter property is a method decorated with @property that allows you to access an attribute-like value through a method, but it behaves like a read-only attribute. 
# It's used for encapsulation, computed properties, lazy evaluation, or adding logic (e.g., validation) without changing how the attribute is accessed externally.



# class Person:
#     def __init__(self, name, age):
#         self.__name = name          # Private attribute
#         self.__age = age            # Private attribute

#     @property
#     def name(self):                 # Getter property
#         return self.__name

#     @property
#     def age(self):                  # Getter property with validation
#         return self.__age

#     @age.setter
#     def age(self, value):           # Setter for age
#         if value >= 0:
#             self.__age = value
#         else:
#             print("Age cannot be negative.")

#     # No setter for name in this example (read-only)
            
# person1 = Person("John", 30)
# print(person1.name)  # Accessing via property (like an attribute)
# print(person1.age)   # Accessing via property
# person1.age = 25     # Modifying via setter
# print(person1.age)    
# person1.age = -5     # Triggers validation
# print(person1.age)
# person1.name = "Alice"  # AttributeError: can't set attribute (no setter defined)

#-------------------------------------------------- 8th example -----------------------------------------------------
# Static Attributes (Class Attributes)

# class Dog:
#     species = "Canine"  # Static attribute (shared by all instances)
#     total_dogs = 0      # Static counter

#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         Dog.total_dogs += 1  # Increment shared counter

#     def bark(self):
#         print(f"{self.name} says: Woof! Species: {Dog.species}")

# # Accessing static attributes
# print(Dog.species)      # Via class: Canine
# print(Dog.total_dogs)   # Via class: 0

# dog1 = Dog("Tommy", "Bulldog")
# print(dog1.species)    # Via instance: Canine
# print(Dog.total_dogs)  # Shared counter: 1
# dog1.bark()            # Uses static attribute

# dog2 = Dog("Rocky", "Labrador")
# print(dog2.species)     # Via instance: Canine
# print(Dog.total_dogs)   # Shared counter: 2
# dog2.bark()             # Uses static attribute

# # Modifying static attribute via class (affects all)
# Dog.species = "Mammal"
# print(dog1.species)     # Mammal
# print(dog2.species)     # Mammal

# # Instance attribute shadows class attribute
# dog1.species = "Pet"    # Creates instance attribute
# print(dog1.species)     # Pet (instance)
# print(dog2.species)     # Mammal (class)
# print(Dog.species)      # Mammal (class)

#-------------------------------------------------- 9th example -----------------------------------------------------
# Static Attributes (Class Attributes)
# In Python, static methods are methods that belong to the class rather than any instance. 
# They are defined using the @staticmethod decorator and don't access self (instance) or cls (class).

# class Dog:
#     species = "Canine"  # Static attribute (shared by all instances)
#     total_dogs = 0      # Static counter

#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         Dog.total_dogs += 1  # Increment shared counter

#     def bark(self):
#         print(f"{self.name} says: Woof! Species: {Dog.species}")

#     @staticmethod
#     def is_dog_sound(sound):  # Static method
#         dog_sounds = ["woof", "bark", "growl"]
#         return sound.lower() in dog_sounds

# # Accessing static attributes
# print(Dog.species)      # Via class: Canine
# print(Dog.total_dogs)   # Via class: 0

# dog1 = Dog("Tommy", "Bulldog")
# print(dog1.species)    # Via instance: Canine
# print(Dog.total_dogs)  # Shared counter: 1
# dog1.bark()            # Uses static attribute

# dog2 = Dog("Rocky", "Labrador")
# print(dog2.species)     # Via instance: Canine
# print(Dog.total_dogs)   # Shared counter: 2
# dog2.bark()             # Uses static attribute

# # Modifying static attribute via class (affects all)
# Dog.species = "Mammal"
# print(dog1.species)     # Mammal
# print(dog2.species)     # Mammal

# # Instance attribute shadows class attribute
# dog1.species = "Pet"    # Creates instance attribute
# print(dog1.species)     # Pet (instance)
# print(dog2.species)     # Mammal (class)
# print(Dog.species)      # Mammal (class)

# # Using static method
# print(Dog.is_dog_sound("woof"))  # True (called on class)
# print(dog1.is_dog_sound("meow")) # False (called on instance)

#-------------------------------------------------- 10th example -----------------------------------------------------
# Access modifiers: public, protected, private
# In Python, protected methods are methods intended for internal use within the class, its subclasses, or the module. 
# They are conventionally prefixed with a single underscore

# class User:
#     def __init__(self, username, email):
#         self.username = username           # Public attribute
#         self._email = email                # Protected attribute (convention)
#         self.__password = "secret"         # Private attribute (name mangled)

#     def _protected_method(self):         # Protected method
#         print("This is a protected method.")

#     def __private_method(self):          # Private method
#         print("This is a private method.")

#     def public_method(self):
#         self._protected_method()  # Calling protected method internally
#         print("Public method calling protected one.")

# class Admin(User):  # Subclass
#     def admin_task(self):
#         self._protected_method()  # Accessing protected method from subclass
#         print("Admin accessing protected method.")

# user1 = User("john_doe", "john@example.com")
# user1.public_method()  # Calls protected method internally

# admin1 = Admin("admin", "admin@example.com")
# admin1.admin_task()    # Subclass accesses protected method

# # Direct access (discouraged but possible)
# user1._protected_method()  # Works, but breaks convention

#-------------------------------------------------- 11th example -----------------------------------------------------
# Encapsulation means binding data and methods that operate on that data within a single unit or class, 
# restricting direct access to some of the object's components.
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number  
#         self.balance = balance                  

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: {amount}. New balance: {self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew: {amount}. New balance: {self.balance}")
#         else:
#             print("Insufficient funds or invalid withdrawal amount.")

#     def get_balance(self):
#         return self.balance
    
# bankaccount1 = BankAccount("123456789", 1000)   
# bankaccount1.deposit(5000)
# bankaccount1.withdraw(2000)
# print(f"Current Balance: {bankaccount1.get_balance()}")

#-------------------------------------------------- 12th example -----------------------------------------------------
# Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object.

# class EmailServices:
#     def _connect(self):
#         print("Connecting to email server...")
        
#     def _authenticate(self):  
#         print("Authenticating user...")
    
#     def send_email(self, to_address, subject, body):
#         self._connect()           
#         self._authenticate()       
#         print(f"Sending email to: {to_address}\nSubject: {subject}\nBody: {body}")   
#         self._disconnect()  
        
#     def _disconnect(self):
#         print("Disconnecting from email server...")

# email1 = EmailServices()
# email1.send_email("user@example.com", "Hello", "This is a test email.")

#---------------------------------------- 13th example ----------------------------------------------------
# Inheritance means a class (child class) can inherit attributes and methods from another class (parent class).

# class Vehicle:
    
#     def __init__(self,brand,model,year):
#         self.model = model
#         self.brand = brand
#         self.price = year
    
#     def start(self):
#         print("Vehicle is stopped")
    
#     def stop(self) :
#         print("Vehicle stopped.")   
        
#     def display_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.price}")    
        
        
# class Car(Vehicle):
#     def __init__(self,brand,model,year,doors,engine_type):
#         super().__init__(brand,model,year)
#         self.doors = doors
#         self.engine_type = engine_type
        
#     def display_info(self):      
#         super().display_info()
#         print(f"Doors: {self.doors}, Engine Type: {self.engine_type}")    

# class Bike(Vehicle):
#     def __init__(self,brand,model,year,type_of_bike):
#         super().__init__(brand,model,year)
#         self.type_of_bike = type_of_bike         
        
#     def display_info(self):      
#         super().display_info()
#         print(f"Type of Bike: {self.type_of_bike}")

# class Truck(Vehicle):
#     def __init__(self,brand,model,year,capacity):
#         super().__init__(brand,model,year)
#         self.capacity = capacity
        
#     def display_info(self):      
#         super().display_info()
#         print(f"Capacity: {self.capacity}")    

# car1 = Car("Toyota","Camry",2020,4,"V6")
# car1.start()
# car1.stop()
# car1.display_info()
# print(car1.__dict__)

# bike1 = Bike("Yamaha","YZF-R3",2021,"Sport")
# bike1.start()   
# bike1.stop()
# bike1.display_info()

# truck1 = Truck("Ford","F-150",2019,"2 tons")
# truck1.start() 
# truck1.stop()     
# truck1.display_info()           

#-------------------------------------------------- 14th example -----------------------------------------------------
# Polymorphism means the ability to take many forms. In OOP, 
# it refers to the ability of different classes to be treated as instances of the same class through a common interface.

class Cat:
    def sound(self):
        print("Meow Meow")
        
class Cow:
    def sound(self):
        print("Moo Moo")
        
class Sheep:
    def sound(self):
        print("Baa Baa")
        
def animal_sound(animal):
    animal.sound()    
    
cat1 = Cat()
cow1 = Cow()
sheep1 = Sheep()

animal_sound(cat1)
animal_sound(cow1)      
                