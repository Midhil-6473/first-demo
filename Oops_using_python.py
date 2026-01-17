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