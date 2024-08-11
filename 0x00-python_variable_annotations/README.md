0x00. Python - Variable Annotations

Type annotations in Python 3
How you can use type annotations to specify function signatures and variable types
Duck typing
How to validate your code with mypy


Type annotations serve as hints to indicate the types of variables and the types of inputs and outputs for functions and methods. This can make the code more understandable and maintainable, especially in larger projects where clarity is crucial. They are not enforced by the Python interpreter, meaning that the code will still run even if the actual types do not match the annotations


Limitations
While type annotations provide many advantages, they do not enforce type checking at runtime. This means that if a variable is assigned a type that does not match its annotation, Python will not raise an error during execution. Instead, these annotations are primarily for the benefit of developers and tools that analyze the code

Duck typing:

"If it walks like a duck and it quacks like a duck, then it must be a duck."

 allows for more flexible and reusable code by supporting polymorphism, enabling different object types to be used interchangeably as long as they provide the required interface


The presence of required methods or attributes is verified at runtime, not compile-time


exmaple:

class Duck:
    def fly(self):
        print("The duck is flying")

class Airplane:
    def fly(self):
        print("The airplane is flying")

def lift_off(entity):
    entity.fly()

duck = Duck()
airplane = Airplane()

lift_off(duck)     # Output: The duck is flying
lift_off(airplane) # Output: The airplane is flying


In this example, the lift_off() function doesn't care about the specific type of the object passed to it. As long as the object has a fly() method, it can be used interchangeably